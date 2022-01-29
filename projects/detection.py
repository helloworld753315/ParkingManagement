# -*- coding: utf-8 -*-

from importlib.resources import path
import cv2
import numpy as np

import numpy as np
import time
import csv
import pprint
import glob
import os
import sheet

import sys
from pathlib import Path
import caputure
import schedule


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

    caputure.job()
    list_of_files = glob.glob('./projects/images/*')  # * means all if need specific format then *.csv
    latest_file = max(list_of_files, key=os.path.getctime)

    # path = "./projects/images/cap_02.jpg"

    path = latest_file

    img = cv2.imread(path)

    count = 0
    for i in range(len(rois)):
        available = availabilityInfo(img, rois[i][0], rois[i][1], rois[i][2], rois[i][3])
        if available:
            count += 1
    print(count)
    sheet.output(caputure.date(), count)

    

if __name__ == "__main__":
    # 60秒に一回実行
    schedule.every(1).minutes.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
