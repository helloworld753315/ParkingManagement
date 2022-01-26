import cv2
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import time
import csv
import pprint


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


