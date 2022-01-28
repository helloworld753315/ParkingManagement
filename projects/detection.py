from email.mime import image
import cv2

"""
cap = cv2.VideoCapture("./projects/images/vtest.avi")
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

def detector(path="./projects/images/cap_02.jpg"):

    model = cv2.createBackgroundSubtractorMOG2()

    background = cv2.imread("./projects/images/cap_01.jpg")
    img = cv2.imread(path)

    mask = model.apply(background)
    mask = model.apply(img)

    # 輪郭抽出する。
    contours = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

    # 小さい輪郭は除く
    contours = list(filter(lambda x: cv2.contourArea(x) > 500, contours))

    # 輪郭を囲む外接矩形を取得する。
    bboxes = list(map(lambda x: cv2.boundingRect(x), contours))

    # 矩形を描画する。
    for x, y, w, h in bboxes:
        cv2.rectangle(background, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite('./projects/images/return.jpg', background)

"""
# 画像の読み込み
img_src1 = cv2.imread("./projects/images/cap_01.jpg", 1)
img_src2 = cv2.imread("./projects/images/cap_02.jpg", 1)
fgbg = cv2.createBackgroundSubtractorMOG2()
fgmask = fgbg.apply(img_src1)
fgmask = fgbg.apply(img_src2)

# 輪郭抽出する。
contours = cv2.findContours(fgmask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[0]

# 輪郭を囲む外接矩形を取得する。
bboxes = list(map(lambda x: cv2.boundingRect(x), contours))

# 矩形を描画する。
for x, y, w, h in bboxes:
    cv2.rectangle(img_src1, (x, y), (x + w, y + h), (0, 255, 0), 2)

# 検出画像
bg_diff_path = './projects/images/diff.jpg'
cv2.imwrite(bg_diff_path, img_src1)
"""


detector()
