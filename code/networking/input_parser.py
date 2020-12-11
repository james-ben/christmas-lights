import json

from procedures import (twinkler, stripes,
                        strobe, columns,
                        blink, crazy)


procedureChoices = [
	"twinkle",
	"stripes",
	"strobe",
	"columns",
	"crazy",
	"blink",
	"off",
]

directionChoices = [
	"forward",
	"backward",
	"bounce"
]


DEFAULT_BRIGHTNESS = 0.5
DEFAULT_RUN_TIME = 30
DEFAULT_BLINK_TIME = 0.5
DEFAULT_ORDERED = True
DEFAULT_DIRECTION = directionChoices[0]


def getDefaultVal(proc, key):
	if proc == procedureChoices[0]:
		return twinkler.getDefaultValue(key)
	elif proc == procedureChoices[1]:
		return stripes.getDefaultValue(key)
	elif proc == procedureChoices[2]:
		return strobe.getDefaultValue(key)
	# elif proc == procedureChoices[3]:
	# 	return "Not yet implemented!"
	elif proc == procedureChoices[4]:
		return blink.getDefaultValue(key)
	else:
		if key == "brightness":
			return DEFAULT_BRIGHTNESS
		elif key == "run_time":
			return DEFAULT_RUN_TIME
		elif key == "blink_time":
			return DEFAULT_BLINK_TIME
		elif key == "color_ordered":
			return DEFAULT_ORDERED
		elif key == "direction":
			return DEFAULT_DIRECTION
		else:
			return "Error, invalid key!"


def validateProcedure(name):
	if name.lower() in procedureChoices:
		return True
	return False

def validateDirection(name):
	if name.lower() in directionChoices:
		return True
	return False


def makeListOfTwo(val, default):
	"""Makes a list of 2 floating point numbers."""
	if isinstance(val, list):
		if len(val) == 0:
			val.append(default)
		if len(val) == 1:
			# enforce float type
			val = [float(val[0])]
			val.append(val[0])
		else:
			# only look at the first 2 values
			val = [float(val[0]), float(val[1])]
	elif isinstance(val, float):
		val = [val, val]
	elif isinstance(val, int):
		val = [val, val]
	elif isinstance(val, str):
		try:
			val = float(val)
			val = [val, val]
		except ValueError:
			val = [default, default]
	else:
		val = [default, default]
	return val


def sanitizePacket(packet):
	"""Sanitize the JSON packet from the request. Could be one dict or list of dicts."""
	data = json.loads(packet)
	if isinstance(data, dict):
		if not data:
			return "Error, empty dictionary"
		returnData = [handleDict(data)]
	elif isinstance(data, list):
		if not data:
			return "Error, empty list"
		returnData = []
		for d in data:
			if isinstance(d, dict):
				packetData = handleDict(d)
				if isinstance(packetData, str):
					return packetData
				else:
					returnData.append(handleDict(d))
			else:
				return "Error, list contained a non-dictionary item!"
	else:
		return "Error, invalid JSON object type!"

	return returnData


def handleDict(data):
	"""One dictionary at a time.

	Makes sure all values are in acceptable ranges.
	Adds in defaults if they don't exist.
	"""
	returnDict = {}

	# TODO: some keys may accept the special value "random"
	for key, val in data.items():
		if key == "name":
			# validate the procedure name exists
			if validateProcedure(val):
				returnDict[key] = val.lower()
			else:
				return "Procedure name does not exist"
			# early exit for the "off" procedure
			if val.lower() == "off":
				return returnDict

		elif key == "color_set":
			# single color or list of colors (strings)
			if isinstance(val, list):
				if not val:
					return "Empty color set!"
				# must all be strings
				returnDict[key] = val
			elif isinstance(val, str):
				returnDict[key] = [val]

		elif key == "color_ordered":
			if isinstance(val, bool):
				returnDict[key] = val
			else:
				returnDict[key] = True

		elif key == "brightness":
			returnDict[key] = makeListOfTwo(val, DEFAULT_BRIGHTNESS)

		elif key == "run_time":
			if isinstance(val, float):
				returnDict[key] = val
			elif isinstance(val, int):
				returnDict[key] = val
			elif isinstance(val, str):
				# try to convert
				try:
					floatVal = float(val)
					returnDict[key] = floatVal
				except Exception:
					returnDict[key] = DEFAULT_RUN_TIME
			else:
				returnDict[key] = DEFAULT_RUN_TIME

		elif key == "blink_time":
			returnDict[key] = makeListOfTwo(val, DEFAULT_BLINK_TIME)

		elif key == "direction":
			# validate direction names
			if validateDirection(val):
				returnDict[key] = val
			else:
				# if empty string
				if not val:
					returnDict[key] = DEFAULT_DIRECTION
				else:
					return "Invalid direction name"

		elif key == "num_runs":
			if isinstance(val, int):
				returnDict[key] = val
			else:
				returnDict[key] = None

		# procedures can have custom keys, so add those here
		# the checking must be done in the procedure side to make sure it is a valid input
		else:
			returnDict[key] = val

	# now make sure the dictionary has all required values
	if not "name" in returnDict:
		# this one we can't do without
		return "Missing procedure name"

	if not "color_set" in returnDict:
		return "Missing color set"

	if not "color_ordered" in returnDict:
		returnDict["color_ordered"] = getDefaultVal(returnDict["name"], "color_ordered")

	if not "brightness" in returnDict:
		df = getDefaultVal(returnDict["name"], "brightness")
		returnDict["brightness"] = makeListOfTwo(df, df)

	if not "blink_time" in returnDict:
		df = getDefaultVal(returnDict["name"], "blink_time")
		returnDict["blink_time"] = makeListOfTwo(df, df)

	if not "direction" in returnDict:
		df = getDefaultVal(returnDict["name"], "direction")
		returnDict["direction"] = df

	# can be based off of time or number or runs, but not both
	# time gets precedence, but could only have one
	if "run_time" in returnDict:
		if "num_runs" in returnDict:
			# remove this from the dictionary
			returnDict.pop("num_runs")
	else:
		if "num_runs" in returnDict:
			pass
		else:
			returnDict["run_time"] = DEFAULT_RUN_TIME

	return returnDict
