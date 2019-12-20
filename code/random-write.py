import sys
import time
from random import randint, choice

# https://intellij-support.jetbrains.com/hc/en-us/community/posts/115000782850-How-to-set-up-working-directory-in-PyCharm-and-package-import-
from light_utils import interface


def randomColor():
	rand_red = randint(50, 200)
	rand_green = randint(50, 200)
	rand_blue = randint(50, 200)
	return (rand_red, rand_green, rand_blue)

def christmasColor():
	options = [
		(120, 0, 0),
		(0, 120, 0),
		(120, 80, 0),
		(100, 100, 100),
	]
	return choice(options)


def main():
	strand = interface.strand()
	num = strand.num_pixels

	while True:
		nextRand = randint(0, num-1)
		# strand.setPixelColor(nextRand, randomColor())
		strand.setPixelColor(nextRand, christmasColor())
		time.sleep(1)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		sys.exit(0)
