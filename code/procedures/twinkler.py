import time

from light_utils import twinkle

def init_white(strand):
	# init all to random white intensity
	for i in range(strand.num_pixels):
		strand.setPixelColor(i, twinkle.white())
	strand.showPixels()


def twinkle_white(strand, twGroup):
	nextTime = twinkle.twinkleTime()
	time.sleep(nextTime)

	# twinkle group
	for j in range(twGroup):
		strand.setPixelColor(strand.randIdx(), twinkle.white())
	strand.showPixels()


def init_color(strand):
	# init all to random colors
	for i in range(strand.num_pixels):
		strand.setPixelColor(i, twinkle.color())
	strand.showPixels()


def twinkle_color(strand, twGroup):
	nextTime = twinkle.twinkleTime()
	time.sleep(nextTime)

	# twinkle group
	for j in range(twGroup):
		strand.setPixelColor(strand.randIdx(), twinkle.color())
	strand.showPixels()


def colorLoop(strand, twGroup, stopFlag):
	init_color(strand)

	while not stopFlag():
		twinkle_color(strand, twGroup)


def whiteLoop(strand, twGroup, stopFlag):
	init_white(strand)

	while not stopFlag():
		twinkle_white(strand, twGroup)