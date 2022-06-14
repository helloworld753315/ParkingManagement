import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import os
import time
import requests
import shutil
import base64
import datetime
from dotenv import load_dotenv
load_dotenv()

def get_nowtime():
    dt_now = datetime.datetime.now()  # 現在日時
    dt_date_str = dt_now.strftime('%Y/%m/%d %H:%M')
    return dt_date_str

def make_folder(parent_path):
    os.makedirs("images", exist_ok=True)
    os.makedirs(f'./images/{parent_path}', exist_ok=True)

def screen_shot(driver, file_name):
    # Get Screen Shot
    driver.save_screenshot(file_name)

# スクロール処理
def scroll_down(driver, height, speed):
    # ループ処理で少しづつ移動
    for i in range(1, height, speed):
        time.sleep(1)
        driver.execute_script("window.scrollTo(0, " + str(i) + ");")

def save_image(src, file_save_path):

    #Base64エンコードされた画像をデコードして保存する。
    if "base64," in src:
        with open(file_save_path, "wb") as f:
            f.write(base64.b64decode(src.split(",")[1]))

    #画像のURLから画像を保存する。
    else:
        res = requests.get(src, stream=True)
        with open(file_save_path, "wb") as f:
            shutil.copyfileobj(res.raw, f)

def scraping(chrome_driver, search_word):
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--start-fullscreen')
    options.add_argument('--disable-plugins')
    options.add_argument('--disable-extensions')
    options.add_argument("window-size=1920,1080")
    driver = webdriver.Chrome(chrome_driver, options=options)

    driver.implicitly_wait(4)

    url = f'https://www.google.com/search?q={search_word}&tbm=isch'

    # Google画像検索を開く
    driver.get(url)

    speed = 100
    height = 2000
    scroll_down(driver, height, speed)

    driver.implicitly_wait(3)

    # 画像一覧用のxpath
    thumbnails_xpath = '//*[@id="yDmH0d"]/div[2]/c-wiz/div[3]'
    thumbnails_container = driver.find_element_by_xpath(thumbnails_xpath)
    # 拡大画像用のxpath
    images_xpath = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img'
    # 画像一覧の1つ1つの画像class
    image_class = 'Q4LuWd'
    # サムネイルのclass
    thumbnail_class = 'n3VNCb'
    # 閉じるボタン
    close_button_class = 'ggjbN'

    time.sleep(3)

    images = thumbnails_container.find_elements_by_class_name(image_class)

    for image in images:
        src = image.get_attribute("src")
        if not(src == "None"):
            time.sleep(1)
            image.click()
            thumbnail = driver.find_element_by_class_name(thumbnail_class).get_attribute("src")
            name = thumbnail
            print("#########")
            print(name)
            print("#########")
            time.sleep(2)
            button = driver.find_element_by_class_name(close_button_class).click()
            # save_image(thumbnail, file_save_path)

    print("#", len(images))

    
    print("終了します.")
    # ブラウザを終了
    driver.quit()


def main():
    # 検索ワードの指定
    QUERY = os.getenv('QUERY')
    DRIVER_PATH = os.getenv('DRIVER_PATH')

    make_folder(QUERY)
    scraping(DRIVER_PATH, QUERY)

if __name__ == "__main__":
    main()
