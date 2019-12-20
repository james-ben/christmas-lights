from . import interface


class Grid(interface.strand):
	def __init__(self):
		super().__init__()
		pt0 = 37
		pt1 = 63
		pt2 = 83
		self.rows = [(0, pt0), (pt0, pt1), (pt1, pt2), (pt2, self.num_pixels)]

	def __del__(self):
		super().__del__()

	def setRow(self, idx, color):
		for i in range(*self.rows[idx]):
			self.setPixelColor(i, color)
		self.pixels.show()
