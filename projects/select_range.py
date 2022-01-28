from email.mime import image
import numpy as np
import cv2
import pandas as pd
import csv


def range(path):

    """
    img_raw = cv2.imread("./projects/images/" + path)

    #select ROIs function
    ROI = cv2.selectROI('Select ROIs', img_raw, fromCenter=False, showCrosshair=False)

    x1 = ROI[0]
    y1 = ROI[1]
    x2 = ROI[2]
    y2 = ROI[3]

    print('ROI', ROI)

    cols = ['x1', 'y1', 'x2', 'y2']
    df = pd.DataFrame(index=[], columns=cols)
    record = pd.Series([x1, y1, x2, y2], index=df.columns)
    df = df.append(record, ignore_index=True)
    print(df)
    """

    image = cv2.imread("./projects/images/" + path)
    r = cv2.selectROIs('Selector', image, showCrosshair=False, fromCenter=False)


    with open('./projects/csv/input.csv', 'w', newline='') as outf:
        csvw = csv.writer(outf)
        csvw.writerows(r)


range("cap_01.jpg")
