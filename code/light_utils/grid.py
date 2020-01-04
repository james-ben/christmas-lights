from . import interface


class Grid(interface.strand):
	def __init__(self):
		super().__init__()
		pt0 = 37
		pt1 = 63
		pt2 = 83

		self.rows = [(0, pt0), (pt0, pt1), (pt1, pt2), (pt2, self.num_pixels)]
		self.cols = [
			[0, pt1 - 1, pt1, self.num_pixels - 1],
			[1, pt1 - 2, pt1, self.num_pixels - 1],
			[3, pt1 - 3, pt1 + 1, self.num_pixels - 2],
			[4, pt1 - 4, pt1 + 2, self.num_pixels - 3],
			[6, pt1 - 5, pt1 + 3, self.num_pixels - 4],
			[7, pt1 - 6, pt1 + 4, self.num_pixels - 5],
			[8, pt1 - 7, pt1 + 5, self.num_pixels - 6],
			[10, pt1 - 8, pt1 + 6, self.num_pixels - 7],
			[12, pt1 - 10, pt1 + 7, self.num_pixels - 8],
			[14, pt1 - 11, pt1 + 8, self.num_pixels - 9],
			[15, pt1 - 12, pt1 + 9, self.num_pixels - 9],
			[17, pt1 - 13, pt1 + 10, self.num_pixels - 10],
			[18, pt1 - 14, pt1 + 10, self.num_pixels - 10],
			[21, pt1 - 15, pt1 + 11, self.num_pixels - 11],
			[23, pt1 - 17, pt1 + 12, self.num_pixels - 11],
			[25, pt1 - 18, pt1 + 13, self.num_pixels - 12],
			[26, pt1 - 19, pt1 + 14, self.num_pixels - 12],
			[28, pt1 - 20, pt1 + 15, self.num_pixels - 13],
			[30, pt1 - 22, pt1 + 16, self.num_pixels - 14],
			[31, pt1 - 23, pt1 + 17, self.num_pixels - 15],
			[33, pt1 - 24, pt1 + 18, self.num_pixels - 16],
			[36, pt1 - 26, pt1 + 19, self.num_pixels - 17],
		]

		self.num_rows = len(self.rows)
		self.num_cols = len(self.cols)

	def __del__(self):
		super().__del__()

	def setRow(self, idx, color):
		for i in range(*self.rows[idx]):
			self.setPixelColor(i, color)
		self.pixels.show()

	def setColumn(self, idx, color):
		for i in self.cols[idx]:
			self.setPixelColor(i, color)
		self.pixels.show()
