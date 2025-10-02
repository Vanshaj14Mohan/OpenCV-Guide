# So in this section we are gonna cover basic transformations of images.
# Examples of transformations are translation, rotation, resizing, flipping, cropping etc.
import cv2
import numpy as np

img = cv2.imread("Section One\Part Three\Cat_image.jpg")

cv2.imshow("Original Cat Image", img)

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

# We can also rotate an already rotated image
# rotated_again = rotate(rotated, -90)
# cv2.imshow("Rotated Again Image", rotated_again)

# 3: Resizing the image
resized = cv2.resize(img, (500,500), interpolation=cv2.INTER_LINEAR) # (500,500) is the new size
# interpolation can be INTER_AREA, INTER_CUBIC, INTER_LINEAR etc.
cv2.imshow("Resized Image", resized)

# 4: Flipping the image
flip = cv2.flip(img, 1) # 0 for vertical, 1 for horizontal, -1 for both this is basically flip code
cv2.imshow("Flipped Image", flip)

# 5: Cropping the image
cropped_img = img[200:400, 300:500] # img[y1:y2, x1:x2]
cv2.imshow("Cropped Image", cropped_img)

cv2.waitKey(0)
cv2.destroyAllWindows()
