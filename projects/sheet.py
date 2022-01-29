import gspread
import json
from dotenv import load_dotenv
load_dotenv()

import os
key = os.getenv('KEY')
spreadsheet_key = os.getenv('SPREADSHEET_KEY')

#ServiceAccountCredentials：Googleの各サービスへアクセスできるservice変数を生成します。
from oauth2client.service_account import ServiceAccountCredentials

#2つのAPIを記述しないとリフレッシュトークンを3600秒毎に発行し続けなければならない
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#認証情報設定
#ダウンロードしたjsonファイル名をクレデンシャル変数に設定（秘密鍵、Pythonファイルから読み込みしやすい位置に置く）
credentials = ServiceAccountCredentials.from_json_keyfile_name("./projects/" + key, scope)

#OAuth2の資格情報を使用してGoogle APIにログインします。
gc = gspread.authorize(credentials)

#共有設定したスプレッドシートキーを変数[SPREADSHEET_KEY]に格納する。
SPREADSHEET_KEY = spreadsheet_key

#_________________________________


def next_available_row(sheet1):
    str_list = list(filter(None, sheet1.col_values(2)))
    return str(len(str_list) + 1)

def output(value_1, value_2):

    # column = 列
    # value = 書き込む値

    #共有設定したスプレッドシートのシート1を開く
    worksheet = gc.open_by_key(SPREADSHEET_KEY).sheet1

    export_value_1 = value_1
    export_value_2 = value_2

    next_row = next_available_row(worksheet)

    worksheet.update_cell(next_row, 1, export_value_1)
    worksheet.update_cell(next_row, 2, export_value_2)




