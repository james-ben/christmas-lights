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
		self.fade = False

	def parseParams(self, params):
		"""Read all the data from the input dictionary."""
		self.color_set = colors.parseColorSet(params["color_set"])
		self.color_ordered = params["color_ordered"]
		self.brightness = params["brightness"]
		self.blink_time = params["blink_time"]
		self.direction = params["direction"]

		# how long to run
		if "run_time" in params:
			self.run_time = params["run_time"]
			self.num_runs = None
		else:
			self.run_time = None
			self.num_runs = params["num_runs"]

		# params specific to this procedure
		if "fade" in params.keys():
			if isinstance(params["fade"], bool):
				self.fade = params["fade"]
		else:
			# if not specified, don't fade
			self.fade = False
		if "twGroup" in params.keys():
			if isinstance(params["twGroup"], int):
				self.twGroup = params["twGroup"]

	def initStrand(self):
		"""Set all the lights to be a color."""
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			nextColor = next(colorCycle)
			for i in range(self.strand.num_pixels):
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				self.strand.setPixelColor(i, nextColor)
				nextColor = next(colorCycle)
		else:
			for i in range(self.strand.num_pixels):
				nextColor = choice(self.color_set)
				nextColor = colors.colorBrightness(nextColor, self.brightness)
				self.strand.setPixelColor(i, nextColor)

		self.strand.showPixels()

	def run(self, strand, params, stopFlag):
		"""Target for new thread."""
		# initialization
		self.strand = strand
		self.parseParams(params)

		# sometimes we skip initializing the strand to colors
		if not self.fade:
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
