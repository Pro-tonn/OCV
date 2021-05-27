import numpy as np
import cv2

#captures the video 
cap = cv2.VideoCapture(0)

#infinite loop for the video
while True:
    
    #ret = boolean argument to make sure the camera is working
    ret, frame = cap.read()
    width = int(cap.get(3))
    height = int(cap.get(4))
       #line is drawn at | starting| Ending point| Color BGR| Line thickness
    img = cv2.line(frame, (0, 0), (width, height), (125,88,206), 5)

    #Display the video/ recording
    cv2.imshow('Video record', img)

    #stop the camera from working
    if cv2.waitKey(1) == ord('q'):
        break

#release the camera
cap.release()
cv2.destroyAllWindows()


