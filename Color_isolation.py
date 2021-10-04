import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('flower.jpg')   # reading the file
img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #conversion from BGR to HSV

hsv_color1 = np.array([110,50,50])
hsv_color2 = np.array([130,255,255])

mask = cv2.inRange(img_hsv, hsv_color1 , hsv_color2) #masking the image
res = cv2.bitwise_and(img, img,mask = mask)
plt.imshow(mask, cmap='Greys')   # Displaying colormap in B/W :)
plt.show()
