# -*- coding: utf-8 -*-

import cv2
import datetime
import schedule
import time
import os

deviceid = 0  # it depends on the order of USB connection.
capture = cv2.VideoCapture(deviceid)

def date():
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    return strdate

def job():
    dirname = './projects/images'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    ret, frame = capture.read()
    # strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    strdate = date()
    fname = "image_" + strdate + ".jpg"
    cv2.imwrite(os.path.join(dirname, fname), frame)
    print(fname + " is created.")

