from enum import Enum
from random import choice


class Color(Enum):
	Red = (120, 0, 0)
	Green = (0, 120, 0)
	Yellow = (120, 80, 0)
	White = (100, 100, 100)

Off = (0, 0, 0)

choices = list(Color)

def randomColor():
	return choice(choices).value
