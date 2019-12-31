import time
from random import choice
from itertools import cycle

from light_utils import twinkle
from light_utils import colors


class TwinkleLights():
	def __init__(self, twg=5):
		self.timerInterrupt = False
		self.color_set = None
		self.color_ordered = None
		self.brightness = None
		self.blink_time = None
		self.direction = None
		self.run_time = None
		self.num_runs = None
		self.strand = None
		self.twGroup = twg

	def parseParams(self, params):
		self.color_set = colors.parseColorSet(params["color_set"])
		self.color_ordered = params["color_ordered"]
		self.brightness = params["brightness"]
		self.blink_time = params["blink_time"]
		self.direction = params["direction"]

		if "run_time" in params:
			self.run_time = params["run_time"]
			self.num_runs = None
		else:
			self.run_time = None
			self.num_runs = params["num_runs"]

	def initStrand(self):
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			nextColor = next(colorCycle)
			for i in range(self.strand.num_pixels):
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				self.strand.setPixelColor(i, nextColor)
				# thisElem, nextElem = nextElem, next(colorCycle)
				nextColor = next(colorCycle)
		else:
			for i in range(self.strand.num_pixels):
				nextColor = choice(self.color_set)
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				self.strand.setPixelColor(i, nextColor)

		self.strand.showPixels()

	def run(self, strand, params, stopFlag):
		# initialization
		self.strand = strand
		self.parseParams(params)
		self.initStrand()

		# run
		if self.run_time is not None:
			while not stopFlag():
				self.iteration()
				time.sleep(twinkle.getTime(self.blink_time))
		else:
			for _ in range(self.num_runs):
				self.iteration()
				time.sleep(twinkle.getTime(self.blink_time))
				if stopFlag():
					break

	def iteration(self):
		colorCycle = cycle(self.color_set)
		# twinkle some all together
		for _ in range(self.twGroup):
			# get the next color
			if self.color_ordered:
				nextColor = next(colorCycle)
			else:
				nextColor = choice(self.color_set)
			# get intensity
			nextColor = colors.colorBrightness(nextColor, self.brightness)
			self.strand.setPixelColor(self.strand.randIdx(), nextColor)

		self.strand.showPixels()


def init_white(strand):
	# init all to random white intensity
	for i in range(strand.num_pixels):
		strand.setPixelColor(i, twinkle.white())
	strand.showPixels()


def twinkle_white(strand, twGroup):
	nextTime = twinkle.twinkleTime()
	time.sleep(nextTime)

	# twinkle group
	for j in range(twGroup):
		strand.setPixelColor(strand.randIdx(), twinkle.white())
	strand.showPixels()


def init_color(strand):
	# init all to random colors
	for i in range(strand.num_pixels):
		strand.setPixelColor(i, twinkle.color())
	strand.showPixels()


def twinkle_color(strand, twGroup):
	nextTime = twinkle.twinkleTime()
	time.sleep(nextTime)

	# twinkle group
	for j in range(twGroup):
		strand.setPixelColor(strand.randIdx(), twinkle.color())
	strand.showPixels()


def colorLoop(strand, twGroup, stopFlag):
	init_color(strand)

	while not stopFlag():
		twinkle_color(strand, twGroup)


def whiteLoop(strand, twGroup, stopFlag):
	init_white(strand)

	while not stopFlag():
		twinkle_white(strand, twGroup)