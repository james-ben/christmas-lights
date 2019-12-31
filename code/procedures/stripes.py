import time
from random import choice
from itertools import cycle

from light_utils import colors, twinkle


colorList = [c.value for c in colors.choices]


class StripeLights:
	def __init__(self):
		self.timerInterrupt = False
		self.color_set = None
		self.color_ordered = None
		self.brightness = None
		self.blink_time = None
		self.direction = None
		self.run_time = None
		self.num_runs = None
		self.strand = None
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

	def run(self, strand, params, stopFlag):
		# initialization
		print("Initializing stripey lights...")
		self.strand = strand
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
			self.stripeUp(nextColor)
		elif self.direction == "backward":
			# down
			self.stripeDown(nextColor)
		elif self.direction == "bounce":
			# up_down
			self.stripeUp(nextColor)
			self.stripeDown(nextColor)

	def stripeUp(self, color):
		for i in range(self.strand.num_pixels):
			self.strand.setPixelColor(i, color)
			self.strand.showPixels()
			time.sleep(twinkle.getTime(self.blink_time))

	def stripeDown(self, color):
		for i in range(self.strand.num_pixels-1, -1, -1):
			self.strand.setPixelColor(i, color)
			self.strand.showPixels()
			time.sleep(twinkle.getTime(self.blink_time))


def upLoopOrdered(strand, stopFlag):
	while not stopFlag():
		for c in colorList:
			for i in range(strand.num_pixels):
				strand.setPixelColor(i, c)
				strand.showPixels()


def upDownLoopOrdered(strand, stopFlag):
	upFlag = True

	while not stopFlag():
		for c in colorList:
			if upFlag:
				for i in range(strand.num_pixels):
					strand.setPixelColor(i, c)
					strand.showPixels()
				upFlag = False
			else:
				for i in range(strand.num_pixels-1, -1, -1):
					strand.setPixelColor(i, c)
					strand.showPixels()
				upFlag = True
