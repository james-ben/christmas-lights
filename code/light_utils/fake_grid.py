"""Will imitate interface of LED grid so that things can be tested not on the Raspberry Pi."""
from random import randint


class FakeInterface():
	def __init__(self):
		self.num_pixels = 100
		self.pixels = [(0, 0, 0)] * self.num_pixels

	def setAllColor(self, color):
		self.pixels = [color] * self.num_pixels

	def setPixelColor(self, num, color):
		self.pixels[num] = color

	def showPixels(self):
		pass

	def randIdx(self):
		return randint(0, self.num_pixels - 1)


class FakeGrid(FakeInterface):
	def __init__(self):
		super().__init__()
		pt0 = 37
		pt1 = 63
		pt2 = 83
		self.rows = [(0, pt0), (pt0, pt1), (pt1, pt2), (pt2, self.num_pixels)]

	def setRow(self, idx, color):
		for i in range(*self.rows[idx]):
			self.setPixelColor(i, color)
