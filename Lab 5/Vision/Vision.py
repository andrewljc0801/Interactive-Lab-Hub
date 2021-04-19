
#This example is directly copied from the Tensorflow examples provided from the Teachable Machine.

import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np
import cv2
import sys
from gtts import gTTS
import os


# Disable scientific notation for clarity
np.set_printoptions(suppress=True)


def say(message):
    audio_filename = "temp.mp3"
    google_tts = gTTS(message, lang = 'en')
    google_tts.save(audio_filename)
    os.system("/usr/bin/mplayer " + audio_filename)

def assistant(object, last_time_seen):
# Car, Person, Wall, Unrelated    
    if object == 'Car':
        if last_time_seen != 'Car':
            say('Watch out! There is a car in front of you. Ask somebody for help!')
    elif object == 'Person':
        if last_time_seen != 'Person':
            say('There is a person in front of you. Smile and say hi!')
    elif object == 'Wall':
        if last_time_seen != 'Wall':
            say('Turn around! You are facing a wall.')
    elif object == 'Unrelated':
        if last_time_seen != 'Unrelated':
            say('Cannot recognize the object. Maybe ask someone for help.')


img = None
webCam = False
if(len(sys.argv)>1 and not sys.argv[-1]== "noWindow"):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")


# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')
# Load Labels:
labels=[]
f = open("labels.txt", "r")
for line in f.readlines():
    if(len(line)<1):
        continue
    labels.append(line.split(' ')[1].strip())

last_seen = ''

while(True):
    if webCam:
        ret, img = cap.read()

    rows, cols, channels = img.shape
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

    image = Image.open('/home/pi/openCV-examples/data/test.jpg')
    size = (224, 224)
    img =  cv2.resize(img, size, interpolation = cv2.INTER_AREA)
    #turn the image into a numpy array
    image_array = np.asarray(img)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)
    object = str(labels[np.argmax(prediction)])
    assistant(object, last_seen)
    last_seen = object

    if webCam:
        if sys.argv[-1] == "noWindow":
           cv2.imwrite('detected_out.jpg',img)
           continue
        cv2.imshow('detected (press q to quit)',img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cap.release()
            break
    else:
        break

cv2.imwrite('detected_out.jpg',img)
cv2.destroyAllWindows()
