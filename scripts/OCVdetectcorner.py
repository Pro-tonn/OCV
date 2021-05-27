import numpy as np
import cv2

img = cv2.imread('scripts\logo.jpg')
img = cv2.resize(img, (400, 400))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

#Algorithm to record corner| Call img|#'s corner|accuracy| min distance between corners
corners = cv2.goodFeaturesToTrack(gray, 50, 0.01, 10)

#corner is printed as a float point. Below changes the float to int
corners = np.int0(corners)

#Sort through the layer of array 
for corner in corners:
    #filter then to single layer array
    x, y = corner.ravel()
    #draw circle around the corner (Refer to OCVrecord file for comments)
    cv2.circle(img, (x, y), 5, (0,0,255), 1)


#Unnecessary optional
'''for i in range(len(corners)):
    for j in range(i + 1, len (corners)):
        corner1 = tuple(corners[i][0])
        corner2 = tuple(corners[j][0])
        color = tuple(map(lambda x: int(x), np.random.randint(0, 255, size = 3)))
        cv2.line(img, corner1, corner2, color, 1)'''

cv2.imshow("Live", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
