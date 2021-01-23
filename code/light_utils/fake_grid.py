"""Will imitate interface of LED grid so that things can be tested not on the Raspberry Pi."""
import os
import sys
import itertools
import numpy as np
from random import randint

sys.path.append(os.path.abspath("./"))
from .emulated import FakeTree

import pygame


class interface:
	def __init__(self):
		self.num_pixels = 100
		self.pixels = [(0, 0, 0)] * self.num_pixels

	def initTree(self, rows):
		self.fakeTree = FakeTree(rows)

	def setAllColor(self, color):
		self.pixels = [color] * self.num_pixels
		self.fakeTree.fillPixels(color)

	def setPixelColor(self, num, color):
		self.pixels[num] = color
		self.fakeTree.drawPixel(num, color)

	def showPixels(self):
		self.fakeTree.updatePixels()

	def randIdx(self):
		return randint(0, self.num_pixels - 1)

	def __del__(self):
		pygame.quit()


class Grid(interface):
	def __init__(self):
		super().__init__()

		# rows
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

		# Delay super call to init fake tree
		#  because it needs to know about row numbers.
		super().initTree(self.rows)

	def setRow(self, idx, color):
		for i in range(*self.rows[idx]):
			self.setPixelColor(i, color)
		self.fakeTree.updatePixels()

	def setColumn(self, idx, color):
		for i in self.cols[idx]:
			self.setPixelColor(i, color)
		self.fakeTree.updatePixels()
