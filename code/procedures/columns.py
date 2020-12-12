from random import choice
from itertools import cycle, tee

from light_utils import colors
from light_utils import twinkle
from procedures.procedure import Procedure


class ColumnLights(Procedure):
	def __init__(self):
		super().__init__()
		self.forwardList = None
		self.backwardList = None
		self.bounceList = None

	# def parseParams(self, params):
	# 	"""Read all the data from the input dictionary."""

	def nextColor(self):
		if self.color_ordered:
			nextColor = next(self.colorCycle)
		else:
			nextColor = choice(self.color_set)
		# get intensity
		return colors.colorBrightness(nextColor, self.brightness)

	def initStrand(self, grid):
		# optionally wipe
		if not self.fade:
			grid.setAllColor(colors.Off)
			grid.showPixels()

		# set up lists
		if self.forwardList is None:
			# only need to do it once
			self.forwardList = [i for i in range(grid.num_cols)]
			self.backwardList = list(reversed(self.forwardList))
			self.bounceList = self.forwardList[:-1] + self.backwardList[:-1]

	# def columnBounce(self, color):
	# 	for i in range(self.grid.num_cols-1):
	# 		self.grid.setColumn(i, color)
	# 		self.grid.setColumn(i+1, color)
	# 		time.sleep(twinkle.getTime(self.blink_time))
	# 		self.grid.setColumn(i, colors.Off)
	# 	self.grid.setColumn(self.grid.num_cols-1, colors.Off)
	# 	for j in range(self.grid.num_cols-2, 1, -1):
	# 		self.grid.setColumn(j, color)
	# 		self.grid.setColumn(j-1, color)
	# 		time.sleep(twinkle.getTime(self.blink_time))
	# 		self.grid.setColumn(j, colors.Off)

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
			colIter = cycle(self.forwardList)
			# divisor = 2
		elif self.direction == "backward":
			colIter = cycle(self.backwardList)
			# divisor = 2
		elif self.direction == "bounce":
			colIter = cycle(self.bounceList)
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
		i1, i2 = tee(colIter)
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
				# column pick
				nextCol = next(i1)
			else:
				nextTime = 0
				showTrue = False
				nextColor = colors.Off
				# column stays the same here

			# format column string
			nextIdx = "c{}".format(nextCol)

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


presets = [
	{
		"name" : "default columns",
		"type" : "columns",
		"data" : {
			"name": "columns",
			"color_set": ["green", "red", "white"],
			"color_ordered": True,
			"brightness": ["0.5", "0.5"],
			"run_time": 10,
			"blink_time": 0.02,
			"direction": "bounce",
		}
	},
	{
		"name" : "blue columns",
		"type" : "columns",
		"data" : {
			"name": "columns",
			"color_set": ["blue"],
			"color_ordered": True,
			"brightness": ["0.5", "0.5"],
			"run_time": 5,
			"blink_time": 0.02,
			"direction": "forward",
		}
	},
]
