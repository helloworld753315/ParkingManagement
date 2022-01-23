import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time

img = cv2.imread("./projects/images/test_01.jpg")


def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]
    
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)
    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        spots.loc += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)


