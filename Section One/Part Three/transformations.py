# So in this section we are gonna cover basic transformations of images.
import cv2

img = cv2.imread("Section One\Part Three\Cat_image.jpg")

cv2.imshow("Cat Image", img)

cv2.waitKey(0)
cv2.destroyAllWindows()