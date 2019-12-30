import json


DEFAULT_BRIGHTNESS = 0.5
DEFAULT_RUN_TIME = 30
DEFAULT_BLINK_TIME = 0.5


def makeListOfTwo(val, default):
	if isinstance(val, list):
		if len(val) == 0:
			val.append(default)
		if len(val) == 1:
			val.append(val[0])
	elif isinstance(val, float):
		val = [val, val]
	else:
		val = [default, default]
	return val


def sanitizePacket(packet):
	"""Sanitize the JSON packet from the request.

	Makes sure all values are in acceptable ranges.
	Adds in defaults if they don't exist.
	"""
	returnDict = {}

	for key, val in packet.items():
		if key == "name":
			# TODO: validate the procedure name exists
			returnDict[key] = val

		elif key == "color_set":
			# single color or list of colors (strings)
			if isinstance(val, list):
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
			else:
				returnDict[key] = DEFAULT_RUN_TIME

		elif key == "blink_time":
			returnDict[key] = makeListOfTwo(val, DEFAULT_BLINK_TIME)

		elif key == "direction":
			# TODO: validate direction names
			returnDict[key] = val

		elif key == "num_run":
			if isinstance(val, int):
				returnDict[key] = val
			else:
				returnDict[key] = None

	return returnDict