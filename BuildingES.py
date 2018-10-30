#BuildingES.py
#!/usr/bin/python

import cv2  #import the openCV lib to python
import serial #import the pyserial module

#Module -1: Image Processing
hc = cv2.imread('/home/george/PycharmProjects/Embeded image processing system/haarcascade_frontalface_alt2.xml')
img = cv2.imshow('/home/jayneil/beautiful-faces.jpg', 0)
faces = cv2.HaarDetectObjects(img, hc, cv2.CreateMemStorage())
a=1
print(faces)
for (x, y, w, h), n in faces:
    cv2.Rectangle(img, (x, y), (x+w, y+h), 255)
cv2.SaveImage("faces_detected.jpg", img)
dst=cv2.imread('faces_detected.jpg')
cv2.NamedWindow('Face Detected', cv2.CV_WINDOW_AUTOSIZE)
cv2.imshow('Face Detected', dst)
cv2.WaitKey(5000)
cv2.DestroyWindow('Face Detected')

#Module -2: Trigger Pyserial
if faces==[]:

	ser=serial.Serial('/dev/ttyUSB0',9600)
	print(ser)
	ser.write('N')
else:

	ser=serial.Serial('/dev/ttyUSB0',9600)
	print(ser)
	ser.write('Y')

