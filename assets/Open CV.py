import cv2

#color value -1 = Color ignore transparent background
#Color value 0 =  Grayscale images
#Color value 1 = Alpha value most likely with transparent backgrounds
img = cv2.imread('assets\logo.jpg', -1)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()