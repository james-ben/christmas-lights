import itertools

import numpy as np

from . import interface


class Grid(interface.strand):
	def __init__(self):
		super().__init__()
		pt0 = 37
		pt1 = 63
		pt2 = 83

		# There are more rows this year
		pts = [0, 21, 34, 46, 57, 66, 76, 85, 94, 100]
		gen = itertools.tee(pts)
		next(gen[1])
		# https://stackoverflow.com/a/5434936/12940429
		self.rows = [(next(gen[0]), next(gen[1])) for _ in range(len(pts)-1)]

		self.oldCols = [
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

		# init the columns procedurally
		self.num_cols = 6
		self.cols = [[] for _ in range(self.num_cols)]
		for r in self.rows:
			# divide the numbers in each row up into n mostly equal parts
			for i, c in enumerate(np.array_split([x for x in range(*r)], self.num_cols)):
				self.cols[i].extend(c)

		self.num_rows = len(self.rows)

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

	def setOldColumn(self, idx, color):
		for i in self.oldCols[idx]:
			self.setPixelColor(i, color)
		self.pixels.show()
