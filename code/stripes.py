import sys
import time

from light_utils import interface


colors = [
	(120, 0, 0),
	(0, 120, 0),
	(120, 80, 0),
	(100, 100, 100),
]


def main():
	strand = interface.strand()
	num = strand.num_pixels

	while True:
		for c in colors:
			for i in range(num):
				strand.setPixelColor(i, c)
				time.sleep(0.01)


if __name__ == '__main__':
	try:
		main()
	except KeyboardInterrupt as e:
		sys.exit(0)
