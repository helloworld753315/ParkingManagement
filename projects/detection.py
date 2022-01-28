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


"""
# cap = cv2.VideoCapture("./projects/images/vtest.avi")
cap = cv2.VideoCapture(0)
wait_secs = int(1000 / cap.get(cv2.CAP_PROP_FPS))

model = cv2.createBackgroundSubtractorMOG2()

while True:
    ret, frame = cap.read()
    if not ret:
        break

    mask = model.apply(frame)

    # 輪郭抽出する。
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # 小さい輪郭は除く
    contours = list(filter(lambda x: cv2.contourArea(x) > 500, contours))

    # 輪郭を囲む外接矩形を取得する。
    bboxes = list(map(lambda x: cv2.boundingRect(x), contours))

    # 矩形を描画する。
    for x, y, w, h in bboxes:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imshow("Frame", frame)
    cv2.waitKey(wait_secs)

cap.release()
cv2.destroyAllWindows()

"""

"""
def detector(path="./projects/images/cap_02.jpg"):

    model = cv2.createBackgroundSubtractorMOG2()

    # background = cv2.imread("./projects/images/cap_01.jpg")
    img = cv2.imread(path)

    # mask = model.apply(background)
    mask = model.apply(img)

    # 輪郭抽出する。
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # 小さい輪郭は除く
    contours = list(filter(lambda x: cv2.contourArea(x) > 500, contours))

    # 輪郭を囲む外接矩形を取得する。
    bboxes = list(map(lambda x: cv2.boundingRect(x), contours))

    # 矩形を描画する。
    for x, y, w, h in bboxes:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite('./projects/images/return.jpg', img)
"""


def drawRectangle(img, a, b, c, d):
    sub_img = img[b:b + d, a:a + c]

    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)

    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        spots.loc += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)

class spots:
    loc = 0


with open('./projects/csv/input.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

rois = [[int(float(j)) for j in i] for i in rois]

min = 1
max = 2
lowThreshold = 2
highThreshold = 1

path = "./projects/images/cap_01.jpg"

img = cv2.imread(path)

for i in range(len(rois)):
    drawRectangle(img, rois[i][0], rois[i][1], rois[i][2], rois[i][3])


"""

image = cv2.imread("./projects/images/cap_01.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

edges = cv2.Canny(gray, 100, 1020)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

count_objects_image = len(contours)

print("画像内のオブジェクト数：", str(count_objects_image))
"""
