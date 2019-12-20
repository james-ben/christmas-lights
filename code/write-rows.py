import sys
import time

from light_utils import grid
from light_utils import colors


def rowColorTest(g):
	g.setRow(0, colors.Color.Green.value)
	g.setRow(1, colors.Color.Red.value)
	g.setRow(2, colors.Color.Yellow.value)
	g.setRow(3, colors.Color.White.value)

	while True:
		time.sleep(10)


def strobe(g):
	waitTime = 0.25
	options = list(colors.Color)

	while True:
		for c in options:
			for i in range(4):
				g.setRow(i, c.value)
				time.sleep(waitTime)
				g.setRow(i, colors.Off)
			for j in range(2, 0, -1):
				g.setRow(j, c.value)
				time.sleep(waitTime)
				g.setRow(j, colors.Off)


def main():
	g = grid.Grid()
	# rowColorTest(g)
	strobe(g)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		sys.exit(0)
