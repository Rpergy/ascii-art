import cv2 as cv

def image2ascii(image, dimensions):
	image = cv.imread(image)

	greyImage = cv.resize(cv.cvtColor(image, cv.COLOR_RGB2GRAY), dimensions)

	for y in greyImage:
		for x in y:
			if x <= 51:
				print("  ", end = "")
			elif x > 51 and x <= 102:
				print("░░", end = "")
			elif x > 102 and x <= 153:
				print("▒▒", end = "")
			elif x > 153 and x <= 204:
				print("▓▓", end = "")
			elif x > 204:
				print("██", end = "")
		print("")

image2ascii("Images/shrey.jpg", (175, 225))
