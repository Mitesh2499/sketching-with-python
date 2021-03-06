# Let's have fun with Python
# Sketching Using Python

For Sketching, I used python opencv library.

## 1] [Opencv](https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_tutorials.html)
OpenCV (Open Source Computer Vision) is a library of programming functions mainly aimed at real-time computer vision. In simple language it is library used for Image Processing. It is mainly used to do all the operation related to Images.

To install opencv-python

```
pip install opencv-python
```

## 2] Download this repository

* Unzip the repository.
* Open Command Prompt and Navigate to current folder
* drawsketch.py require 4 parameters
    
    1.   ```  -i original image name ```
    2.   ```  -x x value should be odd and integer only ```
    3.   ```  -y y value should be odd and integer only ```
    4.   ```  -s image name to save file (any name with .jpg or .jepg extension) ```
* Example

```  
E:\python\sketch>py drawsketch.py -i 1.jpg -x 13 -y 57 -s dhonisketch.jpg
```

## How it works ? 
```
img_rgb = cv2.imread(img)
cv2.imshow("Original Image ", img_rgb)
```
 1. This is original image

![img](https://github.com/Mitesh2499/sketching-with-python/blob/master/images/original.PNG)

```
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow("Grayscale Image", img_gray)
```
 2. This is Grayscale image

![img](https://github.com/Mitesh2499/sketching-with-python/blob/master/images/gray.PNG)


```
img_gray_inv = 255 - img_gray
cv2.imshow("Invert Grayscale", img_gray_inv)
```
 3. This is inverted grayscale image

![img](https://github.com/Mitesh2499/sketching-with-python/blob/master/images/invert-gray.PNG)

```
img_blur = cv2.GaussianBlur(img_gray_inv, ksize=(x, y),sigmaX=0, sigmaY=0)
cv2.imshow("Blur inverted Grayscale", img_blur)

```
 4. This is blur 

![img](https://github.com/Mitesh2499/sketching-with-python/blob/master/images/blur.PNG)

```
img_blend = dodgeV2(img_gray, img_blur)
cv2.imshow("pencil sketch", img_blend)
```
 5. This is final sketch image

![img](https://github.com/Mitesh2499/sketching-with-python/blob/master/images/sketch.PNG)







