import cv2 as cv
import os
import time

def video2ascii(video, dimensions):
	video = cv.VideoCapture(video)

	frameBuffer = []

	print("Rendering...")
	while (video.isOpened()):
		ret, frame = video.read()
	
		if ret == True:
			greyFrame = cv.resize(cv.cvtColor(frame, cv.COLOR_RGB2GRAY), dimensions)
		
			asciiFrame = ""

			for y in greyFrame:
				for x in y:
					if x <= 64:
						asciiFrame += "░░"
					elif x > 64 and x <= 128:
						asciiFrame += "▒▒"
					elif x > 128 and x <= 192:
						asciiFrame += "▓▓"
					elif x > 192:
						asciiFrame += "██"
				asciiFrame += "\n"
		
			frameBuffer.append(asciiFrame)
		else:
			break

	for i in frameBuffer:
		print(i)
		time.sleep(0.01)
		os.system("clear")

	video.release()

	cv.destroyAllWindows()

video2ascii("Videos/testing.mp4", (110, 150))
