from random import uniform
from numpy import dot

from . import colors


def randomIntensity():
	return uniform(0.0, 1.0)


def color():
	c = tuple(dot(colors.randomColor(), randomIntensity()).astype("uint8"))
	return c


def white():
	return tuple(dot(colors.Color.White.value, randomIntensity()).astype("uint8"))


# how long between twinkles
def twinkleTime():
	return uniform(0.1, 2.0)

# generic range generator
def getTime(val):
	if isinstance(val, float):
		return val
	elif isinstance(val, list):
		if len(val) > 1:
			return uniform(val[0], val[1])

	# otherwise, error
	raise TypeError
