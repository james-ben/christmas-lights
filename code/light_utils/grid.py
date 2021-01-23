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
