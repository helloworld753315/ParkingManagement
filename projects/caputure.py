import cv2
import datetime
import schedule
import time
import os

deviceid = 0  # it depends on the order of USB connection.
capture = cv2.VideoCapture(deviceid)


def job():
    dirname = './projects/images'
    if not os.path.exists(dirname):
        os.mkdir(dirname)
    ret, frame = capture.read()
    strdate = datetime.datetime.now().strftime('%Y%m%dT%H%M%S')
    fname = "image_" + strdate + ".jpg"
    cv2.imwrite(os.path.join(dirname, fname), frame)
    print(fname + " is created.")

    
# 60秒に一回実行
schedule.every(1).minutes.do(job)


while True:
  schedule.run_pending()
  time.sleep(1)
