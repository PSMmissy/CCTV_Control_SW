
import cv2

# np is an alias pointing to numpy library
import numpy as np

# capture frames from a webcam
cap = cv2.VideoCapture(0)


# loop runs if capturing has been initialized
while (1):

    # reads frames from a camera
    ret, frame = cap.read()


    # converting BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)



    hsv_color3 = np.array([5, 50, 50])
    hsv_color4 = np.array([7, 255, 255])


    mask1 = cv2.inRange(hsv, hsv_color3, hsv_color4)


    res1 = cv2.bitwise_and(frame, frame, mask=mask1)

    # Display an original image
    cv2.imshow('Original', mask1)

    #cv2.imshow('MASK', mask)

    cv2.imshow('MASK1', res1)

    # Wait for Esc key to stop
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

# Close the window
cap.release()

# De-allocate any associated memory usage
cv2.destroyAllWindows()
