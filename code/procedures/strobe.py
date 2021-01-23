import time
from random import choice
from itertools import cycle, tee

from light_utils import colors
from light_utils import twinkle
from procedures.procedure import Procedure


class StrobeLights(Procedure):
	def __init__(self):
		super().__init__()
		self.forwardList = None
		self.backwardList = None
		self.bounceList = None

	# def parseParams(self, params):
	# 	"""Read all the data from the input dictionary."""

	def initStrand(self, grid):
		# optionally wipe
		if not self.fade:
			grid.setAllColor(colors.Off)
			grid.showPixels()

		# set up lists
		if self.forwardList is None:
			# only need to do it once
			self.forwardList = [i for i in range(grid.num_rows)]
			self.backwardList = list(reversed(self.forwardList))
			self.bounceList = self.forwardList[:-1] + self.backwardList[:-1]

	def iteration(self, stopEvent):
		"""A generator which will return the next commands to do.

		Returns a tuple (idx, color, time, show)
		where idx is the index of a pixel (could by "rand"),
		color is a RGB tuple, already scaled by brightness
		time is how long to sleep before next update
		and show is boolean whether or not to flush updates to strand
		"""

		# direction
		if self.direction == "forward":
			rowIter = cycle(self.forwardList)
			# divisor = 2
		elif self.direction == "backward":
			rowIter = cycle(self.backwardList)
			# divisor = 2
		elif self.direction == "bounce":
			rowIter = cycle(self.bounceList)
			# divisor = 3

		# colors
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			colorFunc = next
		else:
			colorCycle = self.color_set
			colorFunc = choice

		# counters
		# cur_runs = 0
		iterCount = 0

		# iterators
		i1, i2 = tee(rowIter)
		# next(i2)

		# set up complete, begin yielding instructions
		while not stopEvent.is_set():
			# how much time to sleep next
			if (iterCount % 2) == 0:
				nextTime = twinkle.getTime(self.blink_time)
				showTrue = True
				# color pick
				nextColor = colorFunc(colorCycle)
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				# row pick
				nextRow = next(i1)
			else:
				nextTime = 0
				showTrue = False
				nextColor = colors.Off
				# row stays the same here

			# format row string
			nextIdx = "r{}".format(nextRow)

			# next instruction
			yield (nextIdx, nextColor, nextTime, showTrue)

			# update counters
			iterCount += 1

			# doing based on runs, not time
			if (self.num_runs is not None) and ((iterCount // 2) == self.num_runs):
				stopEvent.set()


	def run(self, grid, params, stopEvent):
		"""Run this procedure with the given parameters until stopEvent is set.

		stopEvent is a threading Event.
		Will call parseParams(), and initStrand() if fade is not true.
		Returns a generator to tell what light to change next.
		"""
		self.parseParams(params)
		self.initStrand(grid)

		# return a generator
		return self.iteration(stopEvent)

	# def strobeBounce(self, color):
	# 	for i in range(self.grid.num_rows):
	# 		self.grid.setRow(i, color)
	# 		time.sleep(twinkle.getTime(self.blink_time))
	# 		self.grid.setRow(i, colors.Off)
	# 	for j in range(self.grid.num_rows-2, 0, -1):
	# 		self.grid.setRow(j, color)
	# 		time.sleep(twinkle.getTime(self.blink_time))
	# 		self.grid.setRow(j, colors.Off)



# preset procedures that the client can request
presets = [
	{
		"name" : "strobe bounce",
		"type" : "strobe",
		"data" : {
			"name": "strobe",
			"color_set": ["green", "red", "white"],
			"color_ordered": True,
			"brightness": ["0.5", "0.5"],
		    "run_time": 10,
			"blink_time": ["0.2", "0.2"],
			"direction": "bounce",
		}
	},
	{
		"name" : "strobe up",
		"type" : "strobe",
		"data" : {
			"name": "strobe",
			"color_set": ["green", "red", "white"],
			"color_ordered": True,
			"brightness": ["0.5", "0.5"],
		    "run_time": 10,
			"blink_time": ["0.2", "0.2"],
			"direction": "forward",
		}
	},
	{
		"name" : "strobe down blue",
		"type" : "strobe",
		"data" : {
			"name": "strobe",
			"color_set": ["blue"],
			"color_ordered": True,
			"brightness": ["0.5", "0.5"],
		    "run_time": 10,
			"blink_time": ["0.2", "0.2"],
			"direction": "forward",
		}
	},
]

def getDefaultValue(key):
	"""Gets a default value for a given key. Returns None if key does not exist."""
	d = presets[0]["data"]
	if key in d.keys():
		return d[key]
	else:
		return None
