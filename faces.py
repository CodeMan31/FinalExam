import numpy as np
import cv2 as cv
import pickle

findfaces = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
recognizer = cv.face.LBPHFaceRecognizer_create()    # creates recognizer
recognizer.read("train.yml")    # reads learned data from trainer file

labels = {}     # creates a dictionary for labels
with open("labels.pickle", 'rb') as f:  # opens pickle file to read
    oldLabels = pickle.load(f)      # loads old labels
    labels = {v: k for k, v in oldLabels.items()}   # switches numbers with names
cap = cv.VideoCapture(0)    # captures video stream

while True:
    ret, frame = cap.read()     # gets frame from video stream
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)    # makes frame gray
    faces = findfaces.detectMultiScale(gray, 1.3, 5)    # finds faces in gray frame
    for (x, y, w, h) in faces:

        roi_gray = gray[y:y + h, x:x + w]   # gets region of interest in gray image
        roi_frame = frame[y:y + h, x:x + w]     # gets region of interest in color image
        _ID, conf = recognizer.predict(roi_gray)    # gets confidence level
        if conf > 40:
            font = cv.FONT_HERSHEY_SIMPLEX  # sets font
            name = labels[_ID]  # sets name to ID label
            colorF = (255, 255, 255)    # white
            cv.putText(frame, name, (x, y), font, 1, colorF, 2, cv.LINE_AA)  # writes name by the rectangle

        color = (255, 0, 0)     # BLUE
        cv.rectangle(frame, (x, y), (x + w, y + h), color, 2)   # draws rectangle around face

    cv.imshow('frame', frame)   # shows frame

    if cv.waitKey(1) == ord('q'):   # waits 1 ms if q is pressed it will quit program
        break

cap.release()               # cleanup
cv.destroyAllWindows()
