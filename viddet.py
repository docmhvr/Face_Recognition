import cv2
import time

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

video = cv2.VideoCapture(0)
a=1
while True:
	a+=1
	check,frame = video.read()
	#print(check)
	#print(frame)
	cv2.imshow('Capturing',frame)
	key = cv2.waitKey(1)
	if key ==ord('q'):
		break
print(a)
	#time.sleep(3)
video.release()
cv2.destroyAllWindows()