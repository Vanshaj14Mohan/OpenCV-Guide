# So in this section we are gonna cover basic transformations of images.
# Examples of transformations are translation, rotation, resizing, flipping, cropping etc.
import cv2
import numpy as np

img = cv2.imread("Section One\Part Three\Cat_image.jpg")

cv2.imshow("Cat Image", img)

# 1: Translation means basically means shifting the image along X and Y axis.
def translate(img, x, y): # x is for shifting along X axis and y is for shifting along Y axis
    transMat = np.float32([[1,0,x], [0,1,y]]) # Transformation Matrix
    dimensions = (img.shape[1], img.shape[0]) # width and height of the image
    return cv2.warpAffine(img, transMat, dimensions)

# Values of x and y can be positive or negative.
# +x --> Right
# +y --> Down
# -x --> Left 
# -y --> Up

translated = translate(img, 100, -100)
cv2.imshow("Translated Image", translated)

# 2: Rotation of image
def rotate(img, angle, rotPoint=None):
    (height,width) = img.shape[:2]
    if rotPoint is None:
        rotPoint = (width//2, height//2) # center of the image

    rotPoint = cv2.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 is for scale
    dimensions = (width, height)

    return cv2.warpAffine(img, rotPoint, dimensions)

rotated = rotate(img, 90) # -ve angle for clockwise rotation, +ve for anti-clockwise
cv2.imshow("Rotated Image", rotated)

#     rotPoint = (int(rotPoint[0]), int(rotPoint[1]))
#     rotMat = cv2.getRotationMatrix2D(rotPoint, angle, 1.0) # 1.0 is for scale
#     dimensions = (width, height)
#     return cv2.warpAffine(img, rotMat, dimensions)

# rotated = rotate(img, -45) # -ve angle for clockwise rotation
# cv2.imshow("Rotated Image", rotated)


cv2.waitKey(0)
cv2.destroyAllWindows()
