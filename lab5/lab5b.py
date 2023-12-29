import cv2
from cvlib import *
from lab5a import *
import numpy as np
import random

def pixel_constraint(hlow, hhigh, slow, shigh, vlow, vhigh):
    """
    Checks the HSV "color" given the specified input values.
    """
    def constraint(color):
        (h,s,v) = color
        if h > hlow and h < hhigh and \
           s > slow and s < shigh and \
           v > vlow and v < vhigh: #Are we within he set limits?
            return 1
        return 0
    return constraint
"""
# Test 1
is_black = pixel_constraint(0, 255, 0, 255, 0, 10)
is_black((231, 82, 4))
is_black((231, 72, 199))


hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
plane_list = cvimg_to_list(hsv_plane)
is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)

sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))
cv2.imshow('sky', cvlib.greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)
"""

def generator_from_image(img):
    """
    Generates the color scheme from an image, in a list format.
    """
    def getColor(i):

        return img[i]
    return getColor
    
"""
# Test 2
orig_img = cv2.imread("plane.jpg")
orig_list = cvimg_to_list(orig_img)
generator = generator_from_image(orig_list)

new_list = [generator(i) for i in range(len(orig_list))]
cv2.imshow('original', orig_img)
cv2.imshow('new', cvlib.rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
cv2.waitKey(0)
"""

def generator1(index):
    """
    Randomizes the color for black and white
    """
    val = random.random() * 255 if random.random() > 0.99 else 0
    return (val, val, val)


def combine_images(mask_source, condition, generator1, generator2):
    """
    Uses two different images and two generators to build a new image depending on the condition.   
    """
    new_list = []
    mask = [condition(i) for i in mask_source]
    
    for index in range(len(mask)):
        new_list.append(add_tuples( \
        multiply_tuple(generator1(index), mask[index]), multiply_tuple(generator2(index), 1 - mask[index])))
    return new_list


"""
Test 3
hsv_plane = cv2.cvtColor(cv2.imread("plane.jpg"), cv2.COLOR_BGR2HSV)
plane_list = cvimg_to_list(hsv_plane)

is_sky = pixel_constraint(100, 150, 50, 200, 100, 255)
sky_pixels = list(map(lambda x: x * 255, map(is_sky, plane_list)))

cv2.imshow('sky', greyscale_list_to_cvimg(sky_pixels, hsv_plane.shape[0], hsv_plane.shape[1]))
cv2.waitKey(0)
"""


"""
Test 4
orig_img = cv2.imread("plane.jpg")
orig_list = cvimg_to_list(orig_img)

generator = generator_from_image(orig_list)

new_list = [generator(i) for i in range(len(orig_list))]

cv2.imshow('original', orig_img)
cv2.imshow('new', rgblist_to_cvimg(new_list, orig_img.shape[0], orig_img.shape[1]))
cv2.waitKey(0)
"""

def gradient_condition(i):
    """
    Checks if the HSV values are closer to white or black (0 or 1).
    """
    h = i[0] / 255
    s = i[1] / 255
    v = i[2] / 255
    result = ((h + s + v) / 3)
     
    return result
    
"""
Test 5
plane_img = cv2.imread("plane.jpg")
flowers_img = cv2.imread("flowers.jpg")
gradient_img = cv2.imread("gradient.jpg")

plane_img_list = cvimg_to_list(plane_img)
gradient_img_list = cvimg_to_list(gradient_img)
flowers_img_list = cvimg_to_list(flowers_img)

generator2 = generator_from_image(plane_img_list)

generator3 = generator_from_image(flowers_img_list)

result = combine_images(gradient_img_list, gradient_condition, generator3, generator2)

new_img = rgblist_to_cvimg(result, gradient_img.shape[0], gradient_img.shape[1])
cv2.imshow("f", new_img)
cv2.waitKey(0)
"""


