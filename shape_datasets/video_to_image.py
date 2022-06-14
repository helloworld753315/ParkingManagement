from posixpath import basename
import cv2
import os
from dotenv import load_dotenv

def save_all_frames(video_path, dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)
    print(cap.get(cv2.CAP_PROP_FPS))

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    n = 0

    while True:
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
            n += 1
        else:
            return


def save_frame_range(video_path, start_frame, stop_frame, step_frame,
                     dir_path, basename, ext='jpg'):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        return

    os.makedirs(dir_path, exist_ok=True)
    base_path = os.path.join(dir_path, basename)

    digit = len(str(int(cap.get(cv2.CAP_PROP_FRAME_COUNT))))

    for n in range(start_frame, stop_frame, step_frame):
        cap.set(cv2.CAP_PROP_POS_FRAMES, n)
        ret, frame = cap.read()
        if ret:
            cv2.imwrite('{}_{}.{}'.format(base_path, str(n).zfill(digit), ext), frame)
        else:
            return


def main():
    load_dotenv()
    video_path = os.environ['VIDEO_PATH']
    dir_path = os.environ['DIR_PATH']
    basename = os.environ['BASE_NAME']
    ext=os.environ['EXT']
    # save_all_frames('data/temp/sample_video.mp4', 'data/temp/result', 'sample_video_img')
    # save_all_frames(video_path, dir_path, basename, ext)
    save_frame_range(video_path, 0, 900, 20, dir_path, basename)

if __name__ == "__main__":
    main()