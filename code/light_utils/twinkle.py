from random import uniform
from numpy import dot

from . import colors


def randomIntensity():
	return uniform(0.0, 1.0)


def color():
	c = tuple(dot(colors.randomColor(), randomIntensity()).astype("uint8"))
	return c
