import glob
from dotenv import load_dotenv
import os
import shutil

# データセットの配分を計算 : 0.6, 0.2, 0.2のように全体が1になるよう指定
def culc_rate(images, train, test, val):
    images_len = len(images)
    train_lens = int(images_len * train) # trainの画像枚数
    test_lens = int(images_len * test) # testの画像枚数
    val_lens = int(images_len * val) # valの画像枚数
    print(f'画像ファイル数: {images_len}\n配分: {train_lens} {test_lens} {val_lens}')
    train_lens += (images_len - train_lens - test_lens - val_lens)

    return {"train_lens": train_lens, "test_lens": test_lens, "val_lens": val_lens}

# envに指定したフォルダを作成
def make_dir(dataset_path):
    os.makedirs(f'./datasets', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/train', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/test', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/val', exist_ok=True)


# リストを結合して文字列に文字列に変換
def list_to_string(li):
    return "/".join(li)


# 必要なファイルをコピーする
def remove(dataset_path):
    # 画像ファイル
    images = glob.glob("./datasets/**/*[!.txt]")
    # txtファイル
    txts = glob.glob("./datasets/**/*[.txt]")

    # データセットの配分
    datasets_rate = culc_rate(images, 0.6, 0.2, 0.2)

    # train/test/val
    train = []
    test = []
    val = []

    
    for count in range(len(images)):
        # name = image.split("/")[-1].split(".")[0]
        if count < datasets_rate["train_lens"]:
            train.append(images[count])
        elif count < datasets_rate["train_lens"] + datasets_rate["test_lens"]:
            test.append(images[count])
        else:
            val.append(images[count])

    # train/test/valにコピー
    print("train作成...")
    for image in train:
        input_text_path = f'./datasets/{dataset_path}/{image.split("/")[-1].split(".")[0]}.txt'
        output_image_path = f'./tmp/{dataset_path}/train'
        output_text_path = f'./tmp/{dataset_path}/train'
        shutil.copy(image, output_image_path)
        shutil.copy(input_text_path, output_text_path)
    
    print("test作成...")
    for image in test:
        input_text_path = f'./datasets/{dataset_path}/{image.split("/")[-1].split(".")[0]}.txt'
        output_image_path = f'./tmp/{dataset_path}/test'
        output_text_path = f'./tmp/{dataset_path}/test'
        shutil.copy(image, output_image_path)
        shutil.copy(input_text_path, output_text_path)

    print("val作成...")
    for image in test:
        input_text_path = f'./datasets/{dataset_path}/{image.split("/")[-1].split(".")[0]}.txt'
        output_image_path = f'./tmp/{dataset_path}/val'
        output_text_path = f'./tmp/{dataset_path}/val'
        shutil.copy(image, output_image_path)
        shutil.copy(input_text_path, output_text_path)

def main():
    load_dotenv()

    dataset_path = os.environ['CLASSES']
    make_dir(dataset_path)

    remove(dataset_path)

if __name__ == "__main__":
    main()