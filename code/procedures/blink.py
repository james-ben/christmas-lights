from random import choice
from itertools import cycle

from light_utils import twinkle
from light_utils import colors
from procedures.procedure import Procedure


class BlinkLights(Procedure):
	def __init__(self):
		super().__init__()

	# def parseParams(self, params):
	# 	"""Read all the data from the input dictionary."""

	def run(self, strand, params, stopEvent):
		"""Run this procedure with the given parameters until stopEvent is set.

		stopEvent is a threading Event.
		Will call parseParams().
		Returns a generator to tell what light to change next.
		"""

		self.parseParams(params)

		# return a generator
		return self.iteration(stopEvent)

	def iteration(self, stopEvent):
		"""A generator which will return the next commands to do.

		Returns a tuple (idx, color, time, show)
		where idx is special value "all",
		color is a RGB tuple, already scaled by brightness
		time is how long to sleep before next update
		and show is boolean whether or not to flush updates to strand
		"""

		# cur_runs = 0  # just iterCount / 2
		iterCount = 0

		# set up the color order
		if self.color_ordered:
			colorCycle = cycle(self.color_set)
			colorFunc = next
		else:
			colorCycle = self.color_set
			colorFunc = choice

		while not stopEvent.is_set():
			# how much to sleep next
			nextTime = twinkle.getTime(self.blink_time)

			# every other time, color is "off"
			if (iterCount % 2) == 0:
				nextColor = colors.Off
			else:
				nextColor = colorFunc(colorCycle)
				# get intensity
				nextColor = colors.colorBrightness(nextColor, self.brightness)

			# next instruction
			yield ("all", nextColor, nextTime, True)

			# update the counters
			iterCount += 1

			# doing based on runs, not time
			if (self.num_runs is not None) and ((iterCount // 2) == self.num_runs):
				stopEvent.set()



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
