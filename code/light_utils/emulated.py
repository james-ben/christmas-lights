import os
import sys
import time
import threading

import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
DARK_GREEN = (2, 50, 0)


class FakeTree(object):
	def __init__(self):
		self.height = 350
		self.width = 700
		self.size = (self.width, self.height)

		self.screen = None
		self.lights = None

		# draw the lights - rect is (left, top, width, height)
		self.light_width = 5
		self.light_height = 10
		self.pixels = []

		# draw the rows of lights
		self.row0_rects = np.linspace(start=10, stop=self.width-10, num=37, dtype="int")
		# self.row1_rects = np.linspace(start=50, stop=self.width-50, num=63-37, dtype="int")
		self.row1_rects = np.linspace(start=self.width-50, stop=50, num=63-37, dtype="int")
		self.row2_rects = np.linspace(start=100, stop=self.width-100, num=83-63, dtype="int")
		# self.row3_rects = np.linspace(start=120, stop=self.width-120, num=100-83, dtype="int")
		self.row3_rects = np.linspace(start=self.width-120, stop=120, num=100-83, dtype="int")

		# run background loop
		self.running = True
		self.aliveThread = threading.Thread(target=self.runLoop)
		self.aliveThread.start()
		time.sleep(1)

	def __del__(self):
		self.running = False
		self.aliveThread.join()
		pygame.quit()

	def initRow(self, x, y):
		for r in x:
			nextRect = pygame.Rect(r, y, self.light_width, self.light_height)
			pygame.draw.ellipse(self.lights, BLACK, nextRect)
			self.pixels.append((r, y))
		self.screen.blit(self.lights, (0, 0))

	def runLoop(self):
		"""The initialization of the pygame stuff has to be in the same thread."""
		pygame.init()
		self.screen = pygame.display.set_mode(self.size)
		pygame.display.set_caption('O Tannenbaum')
		self.screen.fill(DARK_GREEN)
		self.lights = pygame.Surface(self.size)
		self.lights.fill(DARK_GREEN)

		self.initRow(self.row0_rects, self.height - 80)
		self.initRow(self.row1_rects, self.height - 130)
		self.initRow(self.row2_rects, self.height - 180)
		self.initRow(self.row3_rects, self.height - 230)
		pygame.display.update()

		print("Beginning the running loop...")
		while self.running:
			pygame.event.pump()
			# for event in pygame.event.get():
			# 	if event.type == pygame.QUIT:
			# 		self.running = False
		# print("Finished the running loop.")

	# user accessible functions
	def drawPixel(self, idx, color):
		pygame.draw.ellipse(self.lights, color, pygame.Rect(*self.pixels[idx], self.light_width, self.light_height))

	def updatePixels(self):
		self.screen.blit(self.lights, (0, 0))
		pygame.display.update()
		time.sleep(0.01)

	def fillPixels(self, color):
		for p in range(len(self.pixels)):
			self.drawPixel(p, color)


def main():
	tree = FakeTree()
	tree.drawPixel(4, WHITE)
	tree.drawPixel(87, WHITE)
	tree.updatePixels()

	while tree.running:
		time.sleep(0.1)

	# is_running = True
	# while is_running:
	# 	for event in pygame.event.get():
	# 		if event.type == pygame.QUIT:
	# 			is_running = False


if __name__ == '__main__':
	main()
