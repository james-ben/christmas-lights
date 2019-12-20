import time
import board
import neopixel

pixels = neopixel.NeoPixel(board.D16, 50, brightness=0.2, auto_write=True,pixel_order=neopixel.GRB)

pixels[0] = (100, 0, 0)
pixels[1] = (0, 100, 0)
pixels.show()
print("showing...")
# time.sleep(10)
