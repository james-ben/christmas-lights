import sys
import time
import board
import neopixel
from random import randint, choice

num_pixels = 100

def randomColor():
    rand_red = randint(50, 200)
    rand_green = randint(50, 200)
    rand_blue = randint(50, 200)
    return (rand_red, rand_green, rand_blue)

def christmasColor():
    options = [
        (150, 0, 0),
        (0, 150, 0),
        (100, 100, 0),
    ]
    return choice(options)

pixels = neopixel.NeoPixel(board.D18, num_pixels, brightness=0.2, auto_write=True,pixel_order=neopixel.GRB)

try:
    while True:
        nextRand = randint(0, num_pixels-1)
        # pixels[nextRand] = randomColor()
        pixels[nextRand] = christmasColor()
        time.sleep(1)
except KeyboardInterrupt as e:
	sys.exit(0)
