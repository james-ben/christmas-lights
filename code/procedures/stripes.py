from light_utils import colors


colorList = [c.value for c in colors.choices]


def upLoopOrdered(strand, stopFlag):
	while not stopFlag():
		for c in colorList:
			for i in range(strand.num_pixels):
				strand.setPixelColor(i, c)
				strand.showPixels()


def upDownLoopOrdered(strand, stopFlag):
	upFlag = True

	while not stopFlag():
		for c in colorList:
			if upFlag:
				for i in range(strand.num_pixels):
					strand.setPixelColor(i, c)
					strand.showPixels()
				upFlag = False
			else:
				for i in range(strand.num_pixels-1, -1, -1):
					strand.setPixelColor(i, c)
					strand.showPixels()
				upFlag = True
