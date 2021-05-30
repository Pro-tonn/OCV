import cv2
import numpy as np  

cap = cv2.VideoCapture(0)

#Using a pre-trained algorithm to find faces
face_detect = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

while True:
    ret, frame = cap.read()

    #Changing the comments to grayscale. Required for processing
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_detect.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (1, 255, 1), 3)
        roi_gray = gray[y:y+w, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

    cv2.imshow("Face detection", frame)

    if cv2.waitKey(1) == ord('c'):
        break

cap.release()
cv2.destroyAllWindows()