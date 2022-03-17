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
from dotenv import load_dotenv
load_dotenv()

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

    # Google画像検索を開く
    driver.get("https://www.google.co.jp/imghp?hl=ja")


    # キーワード検索
    input_xpath = '//*[@id="sbtc"]/div/div[2]/input'

    input_element = driver.find_element_by_xpath(input_xpath)
    input_element.send_keys(search_word)
    # driver.find_element_by_xpath(search_xpath).send_keys(Keys.ENTER)
    input_element.send_keys(Keys.ENTER)
    time.sleep(1)

    # 画像一覧用のxpath
    thumbnails_xpath = '//*[@id="yDmH0d"]/div[2]/c-wiz/div[3]'
    thumbnails_container = driver.find_element_by_xpath(thumbnails_xpath)
    # 拡大画像用のxpath
    images_xpath = '//*[@id="Sva75c"]/div/div/div[3]/div[2]/c-wiz/div/div[1]/div[1]/div[2]/div/a/img'
    speed = 100
    height = 1000
    scroll_down(driver, height, speed)
    thumbnails = thumbnails_container.find_elements_by_tag_name('img')
    count = 0
    for thumbnail in thumbnails:
        thumbnail.click()
        time.sleep(1)
        image = driver.find_elements_by_xpath(images_xpath)[0].get_attribute("src")
        print(count, ":", image)
        count += 1
        driver.back()


    
    






    # for thumbnail in 



    """
    # 画像を保存
    for i, link in enumerate(links):
        try:
            img = requests.get(link)
            with open("img/" + "{}.jpg".format(i), "wb") as f:
                f.write(img.content)

            sleep(1)
        except:
            pass
    """

    # ブラウザを終了
    driver.close()


def main():
    # 検索ワードの指定
    SEARCH_WORD = os.getenv('SEARCH_WORD')
    DRIVER_PATH = os.getenv('DRIVER_PATH')

    make_folder(SEARCH_WORD)
    scraping(DRIVER_PATH, SEARCH_WORD)

if __name__ == "__main__":
    main()
