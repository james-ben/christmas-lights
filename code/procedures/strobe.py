import time

from light_utils import colors


colorList = [c.value for c in colors.choices]


class StrobeLights:
	def __init__(self):
		pass


	def run(self, strand, params, stopFlag):
		pass


def rowColorTest(g):
	"""Tests that the rows are set up correctly."""
	g.setRow(0, colors.Color.Green.value)
	g.setRow(1, colors.Color.Red.value)
	g.setRow(2, colors.Color.Yellow.value)
	g.setRow(3, colors.Color.White.value)


def upDownLoopOrdered(grid, stopFlag, waitTime=0.25):
	while not stopFlag():
		for c in colorList:
			for i in range(4):
				grid.setRow(i, c)
				time.sleep(waitTime)
				grid.setRow(i, colors.Off)
			for j in range(2, 0, -1):
				grid.setRow(j, c)
				time.sleep(waitTime)
				grid.setRow(j, colors.Off)
