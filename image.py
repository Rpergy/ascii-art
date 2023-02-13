import cv2 as cv

def image2ascii(image, dimensions):
	image = cv.imread(image)

	greyImage = cv.resize(cv.cvtColor(image, cv.COLOR_RGB2GRAY), dimensions)

	for y in greyImage:
		for x in y:
			if x <= 64:
				print("░░", end = "")
			elif x > 64 and x <= 128:
				print("▒▒", end = "")
			elif x > 128 and x <= 192:
				print("▓▓", end = "")
			elif x > 192 and x <= 255:
				print("██", end = "")
		print("")

image2ascii("Images/shrey.jpg", (100, 150))
