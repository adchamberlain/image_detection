# Use a pre-trained deep learning model to detect faces, gender, and common objects in web-based images. See requirements.txt for package installs needed.  
# 
# Andrew Chamberlain, Ph.D.
# achamberlain.com
#
# September 2019

# Import packages
import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox
import imutils
import numpy as np

# Read in a test image
image = imutils.url_to_image('https://media.glassdoor.com/l/18/c2/39/97/getting-ready-for-the-speaker-series.jpg')

# Show image. 
plt.imshow(image)

### Step 1. Detect gender in faces in image.

# Apply face detection
faces, conf = cv.detect_face(image)

# Add a bounding box on faces.
for face in faces:
    (startX,startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    
    # Draw rectangle over faces.
    cv2.rectangle(image, (startX,startY), (endX,endY), (0,255,0), 2)

# Loop through detected faces, detect gender.
for face in faces:
    
    # Store starting and ending X,Y coordinates for detected faces.
    (startX,startY) = face[0], face[1]
    (endX, endY) = face[2], face[3]
    
    # Crop detected faces.
    face_crop = np.copy(image[startY:endY, startX:endX])

    # Apply gender detection on cropped faces.
    (label, confidence) = cv.detect_gender(face_crop)

    # Choose most confident label.
    ids = np.argmax(confidence)
    label = label[ids]

    # Format label.
    label = "{}: {:.2f}%".format(label, confidence[ids] * 100)

    # Set label placement.
    Y = startY - 10 if startY - 10 > 10 else startY + 10

    # Push labels into image.
    cv2.putText(image, label, (startX, Y), cv2.FONT_HERSHEY_DUPLEX, 1.1, (0, 0, 0), 2)

# Show results of face and gender detection, with confidence scores.          
plt.imshow(image)

### Step 2. Detect other common objects in image, including people. 

# Read in a test image
image = imutils.url_to_image('https://media.glassdoor.com/l/18/c2/39/97/getting-ready-for-the-speaker-series.jpg')

# Dectect common objects in image. 
bbox, label, conf = cv.detect_common_objects(image)

# Draw boxes on objects. 
output_image = draw_bbox(image, bbox, label, conf)

# Show boxes on object. 
plt.imshow(output_image)

# Print vector of labels assigned to the object.
print('Objects found:' + str(label))