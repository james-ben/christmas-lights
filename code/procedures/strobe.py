import time
from random import choice
from itertools import cycle

from light_utils import colors
from light_utils import twinkle


colorList = [c.value for c in colors.choices]


class StrobeLights:
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
		print("Initializing strobe lights...")
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
		# direction
		if self.direction == "forward":
			# up
			self.strobeUp(nextColor)
		elif self.direction == "backward":
			# down
			self.strobeDown(nextColor)
		elif self.direction == "bounce":
			# bounce
			self.strobeBounce(nextColor)

	def strobeUp(self, color):
		for i in range(4):
			self.grid.setRow(i, color)
			time.sleep(twinkle.getTime(self.blink_time))
			self.grid.setRow(i, colors.Off)

	def strobeDown(self, color):
		for i in range(3, -1, -1):
			self.grid.setRow(i, color)
			time.sleep(twinkle.getTime(self.blink_time))
			self.grid.setRow(i, colors.Off)

	def strobeBounce(self, color):
		for i in range(4):
			self.grid.setRow(i, color)
			time.sleep(twinkle.getTime(self.blink_time))
			self.grid.setRow(i, colors.Off)
		for j in range(2, 0, -1):
			self.grid.setRow(j, color)
			time.sleep(twinkle.getTime(self.blink_time))
			self.grid.setRow(j, colors.Off)


def rowColorTest(g):
	"""Tests that the rows are set up correctly."""
	g.setRow(0, colors.Color.Green.value)
	g.setRow(1, colors.Color.Red.value)
	g.setRow(2, colors.Color.Yellow.value)
	g.setRow(3, colors.Color.White.value)


def upDownLoopOrdered(grid, stopFlag, waitTime=0.25):
	while not stopFlag():
		for c in colorList:
			for i in range(4):
				grid.setRow(i, c)
				time.sleep(waitTime)
				grid.setRow(i, colors.Off)
			for j in range(2, 0, -1):
				grid.setRow(j, c)
				time.sleep(waitTime)
				grid.setRow(j, colors.Off)
