import time
from random import choice
from itertools import cycle

from light_utils import colors, twinkle
from procedures.procedure import Procedure


class StripeLights(Procedure):
	def __init__(self):
		super().__init__()
		self.forwardList = None
		self.backwardList = None
		self.bounceList = None
		self.num_pixels = 0

	# def parseParams(self, params):
	# 	"""Read all the data from the input dictionary."""

	def initStrand(self, strand):
		# optionally wipe
		if not self.fade:
			strand.setAllColor(colors.Off)
			strand.showPixels()

		# set up lists
		if self.forwardList is None:
			# only need to do it once
			self.num_pixels = strand.num_pixels
			self.forwardList = [i for i in range(strand.num_pixels)]
			self.backwardList = list(reversed(self.forwardList))
			self.bounceList = self.forwardList[:-1] + self.backwardList[:-1]

	# def stripeUp(self, color):
	# 	for i in range(self.strand.num_pixels):
	# 		self.strand.setPixelColor(i, color)
	# 		self.strand.showPixels()
	# 		time.sleep(twinkle.getTime(self.blink_time))

	# def stripeDown(self, color):
	# 	for i in range(self.strand.num_pixels-1, -1, -1):
	# 		self.strand.setPixelColor(i, color)
	# 		self.strand.showPixels()
	# 		time.sleep(twinkle.getTime(self.blink_time))

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
			pixelIter = cycle(self.forwardList)
		elif self.direction == "backward":
			pixelIter = cycle(self.backwardList)
		elif self.direction == "bounce":
			pixelIter = cycle(self.bounceList)

		# colors
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			colorFunc = next
		else:
			colorCycle = self.color_set
			colorFunc = choice

		iterCount = 0
		cur_runs = 0
		nextColor = None

		while not stopEvent.is_set():
			nextIdx = next(pixelIter)
			nextTime = twinkle.getTime(self.blink_time)

			if nextIdx == (self.num_pixels-1):
				if (self.direction == "forward") or (self.direction == "bounce"):
					cur_runs += 1
					nextColor = colorFunc(colorCycle)
					nextColor = colors.colorBrightness(nextColor, self.brightness)
			elif nextIdx == 0:
				if (self.direction == "backward") or (self.direction == "bounce"):
					cur_runs += 1
					nextColor = colorFunc(colorCycle)
					nextColor = colors.colorBrightness(nextColor, self.brightness)
			if nextColor is None:
				nextColor = colorFunc(colorCycle)

			# next instruction
			yield (nextIdx, nextColor, nextTime, True)

			if (self.num_runs is not None) and (cur_runs == self.num_runs):
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
		"name" : "stripe default",
		"type" : "stripes",
		"data" : {
			"color_set": ["green", "yellow", "red", "white"],
			"color_ordered": True,
			"brightness": "0.5",
		    "run_time": 5,
			"blink_time": "0.002",
			"name": "stripes",
			"direction": "forward",
		}
	},
	{
		"name" : "stripe random",
		"type" : "stripes",
		"data" : {
			"color_set": ["green", "yellow", "red", "white"],
			"color_ordered": False,
			"brightness": "0.5",
		    "run_time": 5,
			"blink_time": "0.005",
			"name": "stripes",
			"direction": "backward",
		}
	},
	{
		"name" : "stripe bounce",
		"type" : "stripes",
		"data" : {
			"color_set": ["green", "red", "white"],
			"color_ordered": True,
			"brightness": "0.5",
		    "run_time": 5,
			"blink_time": "0.002",
			"name": "stripes",
			"direction": "bounce",
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
