import numpy as np
import cv2 as cv
from time import sleep

# this program just takes a bunch of pictures to be used later


cap = cv.VideoCapture(0)

while True:
    ret, frame = cap.read()
    sleep(9)
    print("look")
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('1.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('2.jpg', frame)
    ret, frame = cap.read()
    sleep(2)
    cv.imwrite('3.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('4.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('5.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('6.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('7.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('8.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('9.jpg', frame)
    ret, frame = cap.read()
    sleep(1)
    cv.imwrite('10.jpg', frame)
    break

cv.destroyAllWindows()  # cleanup
