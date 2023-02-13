import cv2 as cv

image = cv.imread("shrey.jpg")

greyImage = cv.resize(cv.cvtColor(image, cv.COLOR_RGB2GRAY), (150, 250))

print(greyImage)

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
cv.waitKey(0)
