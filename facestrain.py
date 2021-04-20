import cv2 as cv
import os
import numpy as np
from PIL import Image
import pickle

baseDir = os.path.dirname(os.path.abspath(__file__))    # sets base directory to this file
imageDir = os.path.join(baseDir, "images")              # sets up search for images folder
findfaces = cv.CascadeClassifier('haarcascade_frontalface_default.xml')     # classifies the xml for a face
recognizer = cv.face.LBPHFaceRecognizer_create()    # creates recognizer

currentID = 0   # initializes ID at zero, used as a counter
labelIDs = {}   # dictionary for label IDs
yLabels = []    # empty data for ids
xTrain = []     # empty data for roi

for root, dirs, files in os.walk(imageDir):     # for loop that looks through the directory
    for file in files:                          # looks through the files
        if file.endswith("png") or file.endswith("jpg"):    # ensures that only images are looked for
            path = os.path.join(root, file)                 #
            label = os.path.basename(os.path.dirname(path))
            if not label in labelIDs:       # if label isnt applied
                labelIDs[label] = currentID     # sets current ID to labelIDs array
                currentID += 1                  # increments
            _ID = labelIDs[label]
            pilImage = Image.open(path).convert("L")    # converts to grayscale
            imArr = np.array(pilImage, "uint8")         # converts the PIL image to a numpy array

            faces = findfaces.detectMultiScale(imArr, 1.5, 5)   # finds faces in the files

            for (x, y, w, h) in faces:
                roi = imArr[y:y + h, x:x + w]       # grabs the region of interest for image
                xTrain.append(roi)                  # puts it in an array for later
                yLabels.append(_ID)                 # puts ID in array

with open("labels.pickle", 'wb') as f:              # opens pickle file for writing
    pickle.dump(labelIDs, f)                        # puts data label id's in file

recognizer.train(xTrain, np.array(yLabels))         # trains the face recognizer
recognizer.save("train.yml")                        # save trained data to YAML file


