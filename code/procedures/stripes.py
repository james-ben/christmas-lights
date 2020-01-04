import time
from random import choice
from itertools import cycle

from light_utils import colors, twinkle


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

	def run(self, strand, params, stopFlag):
		# initialization
		self.strand = strand
		self.parseParams(params)

		# run
		if self.run_time is not None:
			while not stopFlag():
				self.iteration()
		else:
			for _ in range(self.num_runs):
				self.iteration()
				if stopFlag():
					break

	def iteration(self):
		# direction
		if self.direction == "forward":
			# up
			self.stripeUp(self.nextColor())
		elif self.direction == "backward":
			# down
			self.stripeDown(self.nextColor())
		elif self.direction == "bounce":
			# up_down
			self.stripeUp(self.nextColor())
			self.stripeDown(self.nextColor())

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
