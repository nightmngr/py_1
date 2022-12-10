# python program for face detection from live video stream
# import libraries of python OpenCV
# where its functionality resides
import cv2
# np is an alias pointing to numpy library
import numpy as np
# capture frames from a camera
cap = cv2.VideoCapture(0)   # 0 for default camera
# loop runs if capturing has been initialized.
while 1:
    # reads frames from a camera
    ret, img = cap.read()
    # convert to gray scale of each frames
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Load a cascade file for detecting faces
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    # Detects faces of different sizes in the input image
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
    # To draw a rectangle in a face
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    # Display an image in a window
    cv2.imshow('img',img)
    # Wait for Esc key to stop
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break
# Close the window
cap.release()
# De-allocate any associated memory usage
cv2.destroyAllWindows()

