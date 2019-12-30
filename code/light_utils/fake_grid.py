"""Will imitate interface of LED grid so that things can be tested not on the Raspberry Pi."""
import os
import sys
from random import randint

sys.path.append(os.path.abspath("./"))
from .emulated import FakeTree

import pygame


class interface:
	def __init__(self):
		self.num_pixels = 100
		self.pixels = [(0, 0, 0)] * self.num_pixels
		self.fakeTree = FakeTree()

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
		pt0 = 37
		pt1 = 63
		pt2 = 83
		self.rows = [(0, pt0), (pt0, pt1), (pt1, pt2), (pt2, self.num_pixels)]

	def setRow(self, idx, color):
		for i in range(*self.rows[idx]):
			self.setPixelColor(i, color)
		self.fakeTree.updatePixels()
