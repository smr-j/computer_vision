'''
This code manually greyscales an image using both the average method and the NTSC method. 

'''


# Necessary imports
import numpy as np
import matplotlib.pyplot as plt
import cv2

# Load the image and capture size
flowers = cv2.imread("flowers.jpg")
flowers_grey = cv2.imread("flowers.jpg",cv2.IMREAD_GRAYSCALE)
cv2.imshow("tulips",flowers) # print original tulips (for comparison)
cv2.imshow("greyscale (imread)",flowers_grey) # print opencv greyscale (for comparison)

height, width = flowers.shape[:2]

# Initialize both greyscale matrices
average_grey = np.zeros((height,width),dtype=np.uint8)
ntsc_grey = np.zeros((height,width),dtype=np.uint8)

# Loop over the variables and convert each pixel to greyscale values
for i in range(height):
    for j in range(width):
        # Formulae for greyscale images
        average_grey[i,j] = np.clip(flowers[i,j,0]/3 + flowers[i,j,1]/3 + flowers[i,j,2]/3,0,255)
        ntsc_grey[i,j] = np.clip(flowers[i,j,0] * 0.114 + flowers[i,j,1] * 0.587 + flowers[i,j,2] * 0.299,0,255)
cv2.imshow("greyscale (average)",average_grey) # print average method greyscale
cv2.imshow("greyscale (ntsc)",ntsc_grey) # print ntsc method greyscale
'''
Notes

IMREAD_GRAYSCALE uses the NTSC method.
The NTSC method also seems to preserve color intensity the best.
However, the average method seems to preserve more detail on the lighter tulips while providing an overall darker image.
It feels that the average method creates a 'sharper' image, although this may just be my perception.
(The petal edges on the originally yellow/white tulips are easier to see with the average method's greyscale results.)
'''