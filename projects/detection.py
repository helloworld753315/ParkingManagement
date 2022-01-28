# -*- coding: utf-8 -*-

from importlib.resources import path
import cv2
import numpy as np

import numpy as np
import time
import csv
import pprint

import sys
from pathlib import Path


def availabilityInfo(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]

    lowThreshold = 200
    highThreshold = 800

    gray = cv2.cvtColor(sub_img, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    count_objects_image = len(contours)
    return bool(count_objects_image)


def main():
    with open('./projects/csv/input.csv', 'r', newline='') as inf:
        csvr = csv.reader(inf)
        rois = list(csvr)
        rois = [[int(float(j)) for j in i] for i in rois]

        path = "./projects/images/cap_02.jpg"

    img = cv2.imread(path)

    count = 0
    for i in range(len(rois)):
        available = availabilityInfo(img, rois[i][0], rois[i][1], rois[i][2], rois[i][3])
        print(available)
        if available:
            count += 1
    print(count)
    

if __name__ == "__main__":
    main()
