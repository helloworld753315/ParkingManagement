# -*- coding: utf-8 -*-

from importlib.resources import path
import cv2
import numpy as np

import numpy as np
from PIL import Image
import time
import csv
import pprint

import sys
from pathlib import Path


def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]

    lowThreshold = 200
    highThreshold = 1000

    gray = cv2.cvtColor(sub_img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    count_objects_image = len(contours)
    return bool(count_objects_image)


with open('./projects/csv/input.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

rois = [[int(float(j)) for j in i] for i in rois]

path = "./projects/images/cap_02.jpg"

img = cv2.imread(path)

for i in range(len(rois)):
    drawRectangle(img, rois[i][0], rois[i][1], rois[i][2], rois[i][3])
