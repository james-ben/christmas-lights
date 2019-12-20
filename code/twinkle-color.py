import sys
import time
from random import randint, uniform

from light_utils import interface
from light_utils import twinkle


# how long between twinkles
def twinkleTime():
	return uniform(0.1, 2.0)


def main():
	strand = interface.strand()
	num = strand.num_pixels
	# how many to twinkle at a time
	twGroup = 5

	# init all to random colors
	for i in range(num):
		strand.setPixelColor(i, twinkle.color())

	# mid_white = (70, 70, 70)
	# strand.setAllColor(mid_white)

	while True:
		nextTime = twinkleTime()
		time.sleep(nextTime)

		# twinkle group
		for j in range(twGroup):
			nextRand = randint(0, num - 1)
			strand.setPixelColor(nextRand, twinkle.color())
			strand.showPixels()


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		sys.exit(0)
