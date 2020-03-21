import cv2
import numpy as np
import argparse
import cv2


# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", type=str, required=True,
	help="path to original image")
ap.add_argument("-x", "--xvalue", type=str, required=True,
	help="Value of X should be odd")
ap.add_argument("-y", "--yvalue", type=str, required=True,
	help="Value of Y should be odd")
ap.add_argument("-s", "--save", type=str, required=True,
	help="File name to save")
args = vars(ap.parse_args())
img=args["image"]
x=int(args["xvalue"])
y=int(args["yvalue"])
name=args["save"]

img_rgb = cv2.imread(img)
#cv2.imshow("Original Image ", img_rgb)

img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
#cv2.imshow("Grayscale Image", img_gray)





img_gray_inv = 255 - img_gray
#cv2.imshow("Invert Grayscale", img_gray_inv)
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(x, y),
                            sigmaX=0, sigmaY=0)


#cv2.imshow("Blur inverted Grayscale", img_blur)

def dodgeV2(image, mask):
  return cv2.divide(image, 255-mask, scale=256)

img_blend = dodgeV2(img_gray, img_blur)
#cv2.imshow("pencil sketch", img_blend)

cv2.imwrite(name,img_blend)
