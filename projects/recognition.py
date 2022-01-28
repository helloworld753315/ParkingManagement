# -*- coding: utf-8 -*-

import cv2
import numpy as np
from PIL import Image
import time
import csv
import pprint

import sys
from pathlib import Path
# from IPython.display import Image, display

"""
def reconize():
    with open('./projects/csv/input.csv') as f:
        reader = csv.reader(f)
        l = [list(map(int, row)) for row in reader]

    # 画像入力
    img = cv2.imread("./projects/images/test_02.jpg")

    print(img.shape)    

    # 処理領域を設定(left(x1), top(y1), right(x2), bottom(y2))
    # roi = (937, 218, 1280, 350)
    roi = (l[0][0], l[0][1], l[0][2], l[0][3])
    print(roi)

    # 出力の初期化(入力画像を複製)
    dst_img = img.copy()

    # ROI領域を抜き出し、抜き出した画像をぼかす
    # [top:bottom, left:right] 順序
    s_roi = img[roi[1]: roi[3], roi[0]: roi[2]]
    s_roi = cv2.blur(s_roi, (30, 30))  # ぼかし処理

    #　出力画像の同じ箇所に埋め込み
    dst_img[roi[1]: roi[3], roi[0]: roi[2]] = s_roi

    # ぼかした領域をわかりやすくするために入力画像に矩形描画
    rect_img = img.copy()
    cv2.rectangle(rect_img, (roi[2], roi[3]), (roi[0], roi[1]), (0, 255, 0), 2)

    # 描画
    cv2.namedWindow("image", cv2.WINDOW_AUTOSIZE | cv2.WINDOW_FREERATIO)
    cv2.namedWindow("dst_image", cv2.WINDOW_AUTOSIZE | cv2.WINDOW_FREERATIO)
    cv2.imshow("image", rect_img)
    cv2.imshow("dst_image", dst_img)
    cv2.waitKey()

    cv2.destroyAllWindows()


def out_csv():
    with open('./projects/csv/input.csv') as f:
        reader = csv.reader(f)
        l = [list(map(int, row)) for row in reader]
        print(l)



reconize()
"""

"""

with open('./projects/csv/input.csv') as f:
    reader = csv.reader(f)
    l = [list(map(int, row)) for row in reader]
"""

def drawRectangle(img, a, b, c, d):
    lowThreshold = 100
    highThreshold = 200
    sub_img = img[b:b + d, a:a + c]

    edges = cv2.Canny(sub_img, lowThreshold, highThreshold)
    pix = cv2.countNonZero(edges)

    if pix in range(min, max):
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 255, 0), 3)
        spots.loc += 1
    else:
        cv2.rectangle(img, (a, b), (a + c, b + d), (0, 0, 255), 3)

def callback(foo):
    pass

cv2.namedWindow('parameters')
cv2.createTrackbar('Threshold1', 'parameters', 186, 700, callback)
cv2.createTrackbar('Threshold2', 'parameters', 122, 700, callback)
cv2.createTrackbar('Min pixels', 'parameters', 100, 1500, callback)
cv2.createTrackbar('Max pixels', 'parameters', 323, 1500, callback)

class spots:
    loc = 0

with open('./projects/csv/input.csv', 'r', newline='') as inf:
    csvr = csv.reader(inf)
    rois = list(csvr)

rois = [[int(float(j)) for j in i] for i in rois]
VIDEO_SOURCE = 0
cap = cv2.VideoCapture(VIDEO_SOURCE)

while True:
    spots.loc = 0

    ret, frame = cap.read()
    ret2, frame2 = cap.read()
    min = cv2.getTrackbarPos('Min pixels', 'parameters')
    max = cv2.getTrackbarPos('Max pixels', 'parameters')
    lowThreshold = cv2.getTrackbarPos('Threshold1', 'parameters')
    highThreshold = cv2.getTrackbarPos('Threshold2', 'parameters')

    for i in range(len(rois)):
        drawRectangle(frame, rois[i][0], rois[i][1], rois[i][2], rois[i][3])

    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'Available spots: ' + str(spots.loc), (10, 30), font, 1, (0, 255, 0), 3)
    cv2.imshow('Detector', frame)

    canny = cv2.Canny(frame2, lowThreshold, highThreshold)
    cv2.imshow('canny', canny)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()


"""

# git clone した pytorch_yolov3 ディレクトリのパスを指定してください
yolov3_path = Path("./projects/pytorch_yolov3")

sys.path.append(str(yolov3_path))
from yolov3.detector import Detector

config_path = yolov3_path / "config/yolov3_coco.yaml"
weights_path = yolov3_path / "weights/yolov3.weights"

# 検出器を作成
detector = Detector(config_path, weights_path)

# 画像を読み込む。
img = cv2.imread("./projects/images/sample.png")

# 検出する。
detections = detector.detect_from_imgs(img)

# 車両の検出結果のみ抽出する。
target = ["bicycle", "car", "motorcycle", "cell phone"]
cars = list(filter(lambda x: x["class_name"] in target, detections[0]))

# 検出結果を画像に描画する。
for bbox in cars:
    cv2.rectangle(
        img,
        (int(bbox["x1"]), int(bbox["y1"])),
        (int(bbox["x2"]), int(bbox["y2"])),
        color=(0, 255, 0),
        thickness=2,
    )

for coordinate in l:
    for bbox in cars:
        print(bbox["x1"], bbox["x2"], bbox["y1"], bbox["y2"])
        x = coordinate[0] < int(bbox["x1"]) and int(bbox["x2"]) < coordinate[2] 
        y = coordinate[1] > int(bbox["y1"]) and int(bbox["y2"]) > coordinate[3]
        print(x,y)

"""


# print(len(cars))

# print(cars)

# cv2.imwrite('projects/images/sample_1.png', img)



