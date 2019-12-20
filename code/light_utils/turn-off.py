import board
import neopixel

pixels = neopixel.NeoPixel(board.D18, 100, brightness=0.2, auto_write=True,pixel_order=neopixel.GRB)

# for i in range(50):
#     pixels[i] = (0, 0, 0)

pixels.fill((0, 0, 0))
