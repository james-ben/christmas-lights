from enum import Enum
from random import choice, uniform
from numpy import dot


class Color(Enum):
	Red = (255, 0, 0)
	Green = (0, 255, 0)
	Yellow = (255, 200, 0)
	Blue = (0, 0, 255)
	White = (255, 255, 255)

Off = (0, 0, 0)

colorNameMap = {
	"red"       : Color.Red.value,
	"green"     : Color.Green.value,
	"yellow"    : Color.Yellow.value,
	"blue"      : Color.Blue.value,
	"white"     : Color.White.value,
	"off"       : Off,
}

choices = list(Color)

def randomColor():
	return choice(choices).value

def parseColorSet(colorSet):
	if isinstance(colorSet, str):
		colorSet = [colorSet]
	elif not isinstance(colorSet, list):
		print("Error, color set must be a list!")
		raise TypeError

	returnList = []
	for c in colorSet:
		returnList.append(colorNameMap[c.lower()])

	return returnList

def colorBrightness(color, brightness):
	if isinstance(brightness, float):
		return tuple(dot(color, brightness).astype("uint8"))
	elif isinstance(brightness, list):
		# get random intensity
		intensity = uniform(*brightness)
		return tuple(dot(color, intensity).astype("uint8"))
	else:
		print("Error, invalid brightness type!")
		raise TypeError
