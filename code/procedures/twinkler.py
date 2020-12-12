from random import choice
from itertools import cycle

from light_utils import twinkle
from light_utils import colors
from procedures.procedure import Procedure


class TwinkleLights(Procedure):
	"""Twinkle the lights."""
	def __init__(self, twg=5):
		super().__init__()
		self.twGroup = twg

	def parseParams(self, params):
		"""Read all the data from the input dictionary."""
		super().parseParams(params)
		# params specific to this procedure
		if "twGroup" in params:
			if isinstance(params["twGroup"], int):
				self.twGroup = params["twGroup"]

	def initStrand(self, strand):
		"""Set all the lights to be a color."""
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			nextColor = next(colorCycle)
			for i in range(strand.num_pixels):
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				strand.setPixelColor(i, nextColor)
				nextColor = next(colorCycle)
		else:
			for i in range(strand.num_pixels):
				nextColor = choice(self.color_set)
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				strand.setPixelColor(i, nextColor)

		strand.showPixels()

	def iteration(self, stopEvent):
		"""A generator which will return the next commands to do.

		Returns a tuple (idx, color, time, show)
		where idx is the index of a pixel (could by "rand"),
		color is a RGB tuple, already scaled by brightness
		time is how long to sleep before next update
		and show is boolean whether or not to flush updates to strand
		"""

		cur_runs = 0
		iterCount = 0
		# perhaps could use
		# https://numpy.org/doc/stable/reference/random/generated/numpy.random.Generator.choice.html
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			colorFunc = next
		else:
			colorCycle = self.color_set
			colorFunc = choice

		# this will be changed externally
		while not stopEvent.is_set():
			# how much time to sleep next
			nextTime = twinkle.getTime(self.blink_time)
			# color pick
			nextColor = colorFunc(colorCycle)
			nextColor = colors.colorBrightness(nextColor, self.brightness)
			# update after twGroup assignments have been made
			showTrue = (iterCount % self.twGroup) == 0

			# next instruction
			yield ("rand", nextColor, nextTime, showTrue)

			# update the counters
			iterCount += 1
			if (iterCount % self.twGroup) == 0:
				cur_runs += 1

			# if we're doing the number of runs thing, then it's how many times
			#  a "twinkle group" has finished
			if (self.num_runs is not None) and (cur_runs == self.num_runs):
				stopEvent.set()


	def run(self, strand, params, stopEvent):
		"""Run this procedure with the given parameters until stopEvent is set.

		stopEvent is a threading Event.
		Will call parseParams(), and initStrand() if fade is not true.
		Returns a generator to tell what light to change next.
		"""
		self.parseParams(params)

		if not self.fade:
			self.initStrand(strand)

		# return a generator
		return self.iteration(stopEvent)



# preset procedures
presets = [
	{
		"name" : "twinkle color",
		"type" : "twinkle",
		"data" : {
			"color_set": ["red", "green", "yellow", "white"],
			"color_ordered": False,
			"brightness": ["0", ".5"],
			"run_time": 30,
		    "blink_time": ["0.01", ".5"],
			"name": "twinkle",
		}
	},
	{
		"name" : "twinkle white",
		"type" : "twinkle",
		"data" : {
			"color_set": ["white"],
			"color_ordered": False,
			"brightness": ["0", ".5"],
			"run_time": 30,
		    "blink_time": ["0.01", ".5"],
			"name": "twinkle",
			"fade": True,
		}
	}
]


def getDefaultValue(key):
	"""Gets a default value for a given key. Returns None if key does not exist."""
	d = presets[0]["data"]
	if key in d.keys():
		return d[key]
	else:
		return None
