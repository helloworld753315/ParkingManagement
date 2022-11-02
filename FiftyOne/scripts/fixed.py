# =========データセットの出力形式を修正するスクリプト==========
import glob
from dotenv import load_dotenv
import os
import shutil

# 必要なファイルをコピーする
def copy_dataset(dataset_path):
    # train/test/val
    train = glob.glob(f'./data/{dataset_path}/train/**/*.*[!yaml]', recursive=True)
    test = glob.glob(f'./data/{dataset_path}/test/**/*.*[!yaml]', recursive=True)
    val = glob.glob(f'./data/{dataset_path}/val/**/*.*[!yaml]', recursive=True)

    # train/test/valにコピー
    print("train作成...")
    for data in train:
        output_path = f'./tmp/{dataset_path}/train'
        shutil.copy(data, output_path)
    
    print("test作成...")
    for data in test:
        output_path = f'./tmp/{dataset_path}/test'
        shutil.copy(data, output_path)

    print("val作成...")
    for data in val:
        output_path = f'./tmp/{dataset_path}/val'
        shutil.copy(data, output_path)


# envに指定したフォルダを作成
def make_dir(dataset_path):
    print("出力フォルダ作成...")
    os.makedirs(f'./tmp', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/train', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/test', exist_ok=True)
    os.makedirs(f'./tmp/{dataset_path}/val', exist_ok=True)

def main():
    load_dotenv()
    dataset_path = os.environ['INPUT_DIR']
    make_dir(dataset_path)
    copy_dataset(dataset_path)
    print("作成完了")

if __name__ == "__main__":
    main()
    
    
    

