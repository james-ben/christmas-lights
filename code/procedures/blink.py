import time
from random import choice
from itertools import cycle

from light_utils import twinkle
from light_utils import colors


class BlinkLights():
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
		self.colorCycle = cycle(self.color_set)
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

	def run(self, strand, params, stopFlag):
		"""Target for new thread."""
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
		# get the next color
		if self.color_ordered:
			nextColor = next(self.colorCycle)
		else:
			nextColor = choice(self.color_set)
		# get intensity
		nextColor = colors.colorBrightness(nextColor, self.brightness)

		# blink color
		self.strand.setAllColor(nextColor)
		self.strand.showPixels()
		time.sleep(twinkle.getTime(self.blink_time))

		# turn off
		self.strand.setAllColor(colors.Off)
		self.strand.showPixels()
		time.sleep(twinkle.getTime(self.blink_time))


# preset procedures
presets = [
	{
		"name" : "blink color",
		"type" : "blink",
		"data" : {
			"color_set": ["red", "green", "yellow", "white"],
			"color_ordered": True,
			"brightness": 0.5,
			"run_time": 5,
		    "blink_time": 0.5,
			"name": "blink",
		}
	},
	{
		"name" : "blink green",
		"type" : "blink",
		"data" : {
			"color_set": ["green"],
			"color_ordered": True,
			"brightness": 0.5,
			"run_time": 5,
		    "blink_time": 0.5,
			"name": "blink",
			"fade": True,
		}
	},
	{
		"name" : "blink random",
		"type" : "blink",
		"data" : {
			"color_set": [x for x in list(colors.colorNameMap.keys()) if x != "off"],
			"color_ordered": False,
			"brightness": 0.5,
			"run_time": 10,
			"blink_time": 0.5,
			"name": "blink",
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
