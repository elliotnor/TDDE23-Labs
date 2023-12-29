import cv2
import cvlib
import numpy as np



def cvimg_to_list(img):
    """
    Converts an image to a list of tuples
    """
    img_list = []
    for r in range(img.shape[0]):
        for c in range(img.shape[1]):
            img_list.append(tuple(img[r, c]))
    return img_list


"""
# Test1
import cv2
img = cv2.imread('plane.jpg')

cv2.imshow('img', img)
cv2.waitKey(0)

list_img = cvimg_to_list(img)
cv_img = cvlib.rgblist_to_cvimg(list_img, img.shape[0], img.shape[1])
cv2.imshow("converted", cv_img)

cv2.waitKey(0)
"""




def Negative_gaussian_blur(x, y, s, const):
    """
    Goes through an equation using x and y. "s" stands 
    for 4.5, "const" stands for 1.5, from task description.
    """
    if x == 0 and y == 0:
        return const

    frac = -1/(2*np.pi*s**2)
    exp = np.exp(-(x**2+y**2)/(2*s**2))
    return frac*exp

def unsharp_mask(N):
    """
    Creates a N x N matrix with origo in the center, using 
    the values from Negative_gaussian_blur.
    """
    return [[Negative_gaussian_blur(x, y, 4.5, 1.5) for x in range(-(N//2), - (N//2) + N)]\
        for y in range (-(N//2), -(N//2) + N)]
   
   
"""
# Test2
img = cv2.imread('plane.jpg')
cv2.imshow("start", img)
cv2.waitKey(0)
kernel = np.array(unsharp_mask(11))
filtered_img = cv2.filter2D(img, -1, kernel)
cv2.imshow("filtered", filtered_img)
cv2.waitKey(0)

"""