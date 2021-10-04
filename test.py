import cv2
import numpy as np
import matplotlib.pyplot as plt

cap = cv2.VideoCapture(0)

def nothing():  #Dummy function for the trackbar
    pass

cv2.namedWindow("Trackbar")   #Trackbar window

cv2.createTrackbar("L_H","Trackbar",0,255,nothing) #Lower Hue
cv2.createTrackbar("L_S","Trackbar",0,255,nothing) #Lower Saturation
cv2.createTrackbar("L_V","Trackbar",0,255,nothing) #Lower Value

cv2.createTrackbar("U_H","Trackbar",255,255,nothing) #Upper Hue
cv2.createTrackbar("U_S","Trackbar",255,255,nothing) #Upper Saturation
cv2.createTrackbar("U_V","Trackbar",255,255,nothing) #Upper Value

while(1):
     #Capture the Video Frame By Frame.
    _,frame = cap.read()

    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    L_H = cv2.getTrackbarPos("L_H","Trackbar")
    L_S = cv2.getTrackbarPos("L_S", "Trackbar")
    L_V = cv2.getTrackbarPos("L_V", "Trackbar")

    U_H = cv2.getTrackbarPos("U_H", "Trackbar")
    U_S = cv2.getTrackbarPos("U_S", "Trackbar")
    U_V = cv2.getTrackbarPos("U_V", "Trackbar")

    l_b = np.array([L_H,L_S,L_V]) #Lower-bound value for the Color to be Isolated
    u_b = np.array([U_H,U_S,U_V]) #upper-bound value for the Color to be Isolated

    mask = cv2.inRange(frame,l_b,u_b)  #Masking

    res = cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("ORIGINAL",frame)

    cv2.imshow("MASKED", mask)

    cv2.imshow("RES", res)


    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.waitkey(0)
cv2.distroyAllWindows()




