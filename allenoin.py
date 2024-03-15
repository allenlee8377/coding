#下載-轉換-提取-解析

import os
import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
import random
from bs4 import BeautifulSoup


def download_data(stock_id, start_year, end_year, download_folder):
    # 輸入日期
    start_date = f"00{start_year}0101"
    end_date = f"00{end_year}1231"

    # 設定下載路徑
    download_path = r'C:\K'  # 指定下載目錄

    # 設定 ChromeOptions
    chrome_options = webdriver.ChromeOptions()

    # 設定下載路徑和關閉下載提示
    prefs = {"download.default_directory": download_path, "download.prompt_for_download": False}
    chrome_options.add_experimental_option("prefs", prefs)

    # 初始化 Chrome 瀏覽器傳入 ChromeOptions
    driver = webdriver.Chrome(options=chrome_options)

    driver.get(f"https://goodinfo.tw/tw/ShowK_Chart.asp?STOCK_ID={stock_id}&CHT_CAT=WEEK&PRICE_ADJ=T")

    # 輸入日期
    driver.find_element(By.ID, 'edtSTART_DT').send_keys(start_date)
    driver.find_element(By.ID, 'edtEND_DT').send_keys(end_date)

    # 點擊查詢按鈕
    query_button = driver.find_element(By.XPATH, '//*[@value="查詢"]')
    query_button.click()

    time.sleep(random.randint(3, 5))  # 等待頁面加載

    # 點擊下載按鈕(HTML)
    download_button = driver.find_element(By.XPATH, '//*[@id="divK_ChartDetail"]/table/tbody/tr/td/table/tbody/tr/td[3]/nobr/input[2]')
    download_button.click()

    time.sleep(random.randint(3, 5))  # 等待下載完成

    driver.quit()

    # 確認下載的檔案存在且作運算
    original_file_name = f'K_Chart.html'
    if os.path.isfile(os.path.join(download_path, original_file_name)):
        # 將下載的 .html 檔案更名為 {stock_id}_K_Chart.html
        new_file_name = f"{stock_id}_K_Chart.html"
        os.rename(os.path.join(download_path, original_file_name), os.path.join(download_path, new_file_name))

        # 讀取 新的HTML 檔案
        with open(os.path.join(download_path, new_file_name), 'r', encoding='utf-8') as file:
            html_content = file.read()

        # 使用 BeautifulSoup 解析 HTML
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table')

        # 將 HTML 表格轉換為 DataFrame
        df = pd.read_html(str(table))[0]

        # 選擇並保留特定的行和列
        selected_data = df.iloc[:, 0:8]  # 保留第 1 到第 8 列

        # 將多級索引列轉換為單級索引列
        selected_data.columns = ['_'.join(col) for col in selected_data.columns]

        # 選擇要切割的列（第一列）
        column_to_split = selected_data.iloc[:, 0]

        # 使用 str.split() 將該列中的數值進行切割，並分配到新的列中，會在第9/10列
        split_result = column_to_split.str.split('W', expand=True)
        selected_data['年份'] = split_result[0]
        selected_data['週別'] = 'W' + split_result[1]

        # 定義 if 運算函數，根據漲跌分類
        def if_operation(value):
            if value > 0:
                return 1
            elif value < 0:
                return -1
            elif value == 0:
                return 0
            else:
                return "N/A"

        # 將多級索引列轉換為單級索引列
        #df.columns = ['_'.join(col) for col in df.columns]
        # 將 if 運算應用於第 8 列，並將結果存儲到新列
        selected_data['漲跌分析'] = selected_data.iloc[:, 7].apply(if_operation)

        # 儲存為 Excel 檔案
        new_file_name = f"{stock_id}_K_Chart_A2H.xlsx"
        #df.to_excel(os.path.join(download_path, new_file_name), index=False)
        selected_data.to_excel(os.path.join(download_path, new_file_name), index=False)

    else:
        print("下載的檔案不存在！")

print("\n:: 此Python執行檔，僅使用抓取股票的週K資料，無任何推薦買賣。")
print(":: 此程式使用須知:")
print(":: 1.免費")
print(":: 2.如有收費都是詐騙，改用任何形式牟取他人利益，會賠光身家。")
print(":: 3.資料下載後請善用樞紐分析")
print(":: Excel 樞紐分析 或 googlesheet 資料透視表，可依照年、週、值(漲跌/高低價)分析")
print(":: 重複的事情交給程式，分析思考靠自己")
print(":: 再次提醒，抓檔前-記得在C槽，新建名稱為 K 的資料夾\n")
print("> 網站每次最多提供5年的資料，例如輸入2019，會下載20191231-20150101")
print("> 想要抓更多年的資料，就抓n次，自行合併\n")


def main():
    while True:
        download_path = r'C:\K'  # 指定下載目錄
        stock_id = input(">> 請輸入股票代號_ex: 2330：")
        end_year = int(input(">> 請輸入結束年份_ex:2023："))
        start_year = end_year - 4
        download_folder = "C:/K/"  # 將路徑替換為您希望保存文件的目錄
        download_data(stock_id, start_year, end_year, download_folder)

        print("\n# 警告訊息不用理會 #\n")
        # 列出下載資料夾中的所有檔案
        downloaded_files = os.listdir(download_path)
        print("\nK資料夾中的檔案：\n", downloaded_files)

        choice = input("\n>> 是否繼續新的下載？(y/n): ")
        if choice.lower() != 'y':
            break

if __name__ == "__main__":
    main()


'''
if __name__ == "__main__":
    stock_id = input(">> 請輸入股票代號_ex: 2330：")
    end_year = int(input(">> 請輸入結束年份_ex:2023："))
    start_year = end_year - 4
    download_folder = "C:/K/"  # 將路徑替換為您希望保存文件的目錄
    download_data(stock_id, start_year, end_year, download_folder)
'''