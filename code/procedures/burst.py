"""To be implemented on something that has a higher pixel density."""

from random import choice
from itertools import cycle

from light_utils import colors
from light_utils import twinkle


class BurstLight:
	def __init__(self):
		self.timerInterrupt = False
		self.color_set = None
		self.color_ordered = None
		self.brightness = None
		self.blink_time = None
		self.direction = None
		self.run_time = None
		self.num_runs = None
		self.grid = None
		self.colorCycle = None

	def parseParams(self, params):
		"""Read all the data from the input dictionary."""
		self.color_set = colors.parseColorSet(params["color_set"])
		self.color_ordered = params["color_ordered"]
		self.brightness = params["brightness"]
		self.blink_time = params["blink_time"]
		self.direction = params["direction"]
		self.colorCycle = cycle(self.color_set)

		if "run_time" in params:
			self.run_time = params["run_time"]
			self.num_runs = None
		else:
			self.run_time = None
			self.num_runs = params["num_runs"]

	def nextColor(self):
		if self.color_ordered:
			nextColor = next(self.colorCycle)
		else:
			nextColor = choice(self.color_set)
		# get intensity
		return colors.colorBrightness(nextColor, self.brightness)

	def run(self, grid, params, stopFlag):
		self.grid = grid
		self.parseParams(params)

		# run
		if self.run_time is not None:
			while not stopFlag():
				self.iteration(self.nextColor())
		else:
			for _ in range(self.num_runs):
				self.iteration(self.nextColor())
				if stopFlag():
					break

	def iteration(self, nextColor):
		pass
