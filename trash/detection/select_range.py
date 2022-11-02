from email.mime import image
import numpy as np
import cv2
import pandas as pd
import csv


def range(path):
    image = cv2.imread("./projects/images/" + path)
    r = cv2.selectROIs('Selector', image, showCrosshair=False, fromCenter=False)

    with open('./projects/csv/input.csv', 'w', newline='') as outf:
        csvw = csv.writer(outf)
        csvw.writerows(r)


range("image_20220129T113350.jpg")
