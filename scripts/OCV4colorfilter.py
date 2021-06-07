import numpy as np
import cv2

#captures the video 
cap = cv2.VideoCapture(0)

#infinite loop for the video
while True:
    ret, frame = cap.read()
    #max value for width
    width = int(cap.get(3))
    #max value for height
    height = int(cap.get(4))

    #saturates the image from BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    #min value for the color
    lower_color = np.array([90, 50, 50])
    #max value for the color
    #Both of the value are set to blue
    upper_color = np.array([130, 255, 255])

    #unify the saturated image with the max and min value of colors
    mask = cv2.inRange(hsv, lower_color, upper_color)

    #Detect color within the max and min value of color
    result = cv2.bitwise_and(frame, frame, mask=mask)

    #optional resizing video for better view
    frame = cv2.resize(frame, (400, 400))
    mask = cv2.resize(mask, (400, 400))
    result = cv2.resize(result, (400, 400))

    #Display the corresponding images
    cv2.imshow('Blue detection', result)
    cv2.imshow('White and Black', mask)
    cv2.imshow('Main video', frame)

    #stop the camera from working
    if cv2.waitKey(1) == ord('c'):
        break

#release the camera
cap.release()
cv2.destroyAllWindows()
