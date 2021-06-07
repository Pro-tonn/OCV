import numpy as np
import cv2

#captures the video 
cap = cv2.VideoCapture(0)

#infinite loop for the video
while True:
    
    #ret = boolean argument to make sure the camera is working
    ret, frame = cap.read()
    #max value for width
    width = int(cap.get(3))
    #max value for height
    height = int(cap.get(4))

       #line is drawn at | starting| Ending point| Color BGR| Line thickness
    #img = cv2.line(frame, (0, 0), (width, height), (125,88,206), 5)

    img = cv2.rectangle(frame, (200, 100), (450, 320), (178, 123, 88), 5 )
                        #Circle center | radius| color | thickness
    #img = cv2.circle(frame, (300, 200), 120, (0,0,255), 5)

    font = cv2.FONT_ITALIC
                        #Display text           Location   Font|scale| Color | thickness| line type (docs ambiguous) 
    img = cv2.putText(frame, 'Analysing image', (200, 380), font, 1, (0, 0,0), 3, cv2.LINE_AA )

    #Display the video/ recording
    cv2.imshow('Video record', img)

    #stop the camera from working
    if cv2.waitKey(1) == ord('q'):
        break

#release the camera
cap.release()
cv2.destroyAllWindows()


