import cv2

#color value -1 = Color ignore transparent background
#Color value 0 =  Grayscale images
#Color value 1 = Alpha value most likely with transparent backgrounds
img = cv2.imread('scripts\logo.jpg', -1)
img = cv2.resize(img, (400, 400))

#rotational snippet
#img = cv2.rotate(img, cv2.cv2.ROTATE_90_COUNTERCLOCKWISE)

#saving a processed image (including the file format of the image)
#cv2.imwrite('New_img.jpg', img)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()