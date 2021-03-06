import serial
import time
import tensorflow.keras
from PIL import Image, ImageOps
import numpy as np

# Disable scientific notation for clarity
np.set_printoptions(suppress=True)

# Load the model
model = tensorflow.keras.models.load_model('keras_model.h5')

# Model output labels
labels = {0: 'Feliz 😃',
        1: 'Molesto 😡',
        2: 'Triste 😞',
        3: 'Neutro 😐'}

# Create the array of the right shape to feed into the keras model
# The 'length' or number of images you can put into the array is
# determined by the first position in the shape tuple, in this case 1.
data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)

# Replace this with the path to your image
# import the opencv library 
# References
# https://www.geeksforgeeks.org/python-opencv-capture-video-from-camera/
# https://pythonforundergradengineers.com/python-arduino-LED.html#:~:text=To%20communicate%20with%20the%20Arduino,run%20the%20conda%20install%20command.

import cv2 

# define a video capture object 
vid = cv2.VideoCapture(1) 

ser = serial.Serial('/dev/cu.usbmodem141101', 9800, timeout=1)

curr_sent = labels[0]
  
while(True): 
      
    # Capture the video frame 
    # by frame 
    ret, frame = vid.read()

    image = Image.fromarray(frame)

    #resize the image to a 224x224 with the same strategy as in TM2:
    #resizing the image to be at least 224x224 and then cropping from the center
    size = (224, 224)
    image = ImageOps.fit(image, size, Image.ANTIALIAS)

    #turn the image into a numpy array
    image_array = np.asarray(image)

    # Display the resulting frame 
    cv2.imshow('frame', image_array)

    # Normalize the image
    normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1

    # Load the image into the array
    data[0] = normalized_image_array

    # run the inference
    prediction = model.predict(data)

    sentiment = labels[prediction.argmax()]

    print(sentiment, end='\r')

    if curr_sent == sentiment:
        pass
    else:
        time.sleep(0.5)   # wait 0.5 seconds
        ser.write(f'{sentiment[0]}'.encode())   # send the pyte string 'H'

    curr_sent = sentiment
      
    # the 'q' button is set as the 
    # quitting button you may use any 
    # desired button of your choice 
    if cv2.waitKey(1) & 0xFF == ord('q'): 
        break
  
# After the loop release the cap object 
vid.release() 
# Destroy all the windows 
cv2.destroyAllWindows() 






