import board
import neopixel

class strand(object):
    def __init__(self):
        self.num_pixels = 100
        self.pin_num = board.D18
        self.pixels = neopixel.NeoPixel(self.pin_num, self.num_pixels, auto_write=False, pixel_order=neopixel.RGB)

    def setAllColor(self, color):
        self.pixels.fill(color)

    def setPixelColor(self, num, color):
        self.pixels[num] = color

    def showPixels(self):
        self.pixels.show()

    def __del__(self):
        self.pixels.fill((0, 0, 0))
        self.pixels.show()
        s = super()
        if hasattr(s, "__del__"):
            s.__del__(self)
