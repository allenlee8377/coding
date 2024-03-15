#怒抓三大法人的買賣超情況
import pandas as pd
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm

def three_fund_buyandsell(year_month):
    date = year_month + '01'
    url = f'https://www.twse.com.tw/rwd/zh/fund/TWT47U?date={date}&selectType=ALL&response=html'

    response = requests.get(url)

    # 檢查是否200
    if response.status_code == 200:
        # 解析HTML内容
        soup = BeautifulSoup(response.text, 'html.parser')
        # 找到表格
        table = soup.find('table')
        # 讀取数据
        df = pd.read_html(str(table))[0]

        # 指定的保留直行
        selected_columns = [0, 1, 4, 10, 11, 14, 17]
        df_selected = df.iloc[:, selected_columns]

        # 創建EXCEL檔案
        excel_file = f'C:/K/twse_fund_{year_month}.xlsx'
        with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
            # 寫進EXCEL
            df_selected.to_excel(writer, sheet_name='Sheet1', index=True)

        return excel_file
    else:
        print("建立Excel失敗，:", response.status_code)
        return None

print("\n:: 此Python執行檔，僅使用抓取三大法人某年某月買賣超股數，無任何推薦買賣。")
print(":: 此程式使用須知:")
print(":: 1.免費")
print(":: 2.如有收費都是詐騙，改用任何形式牟取他人利益，會賠光身家。")
print(":: 3.資料下載後請善用樞紐分析，與=if(AND(條件),'Ture','') 的excel函式")
print(":: Excel 樞紐分析 或 googlesheet 資料透視表")
print(":: 重複的事情交給程式，分析思考靠自己")
print(":: 再次提醒，抓檔前-記得在C槽，新建名稱為 K 的資料夾\n")
print("> 輸入201901，會下載2019年1月份三大法人各項產品買賣超")
print("> 想要抓更多年的資料，就抓n次\n")


# 主程式
if __name__ == "__main__":
    year_month = input("請輸入年月（格式：YYYYMM）ex 201901：")
    print("下載中...\n")
    with tqdm(total=100) as pbar:
        excel_file = three_fund_buyandsell(year_month)
        if excel_file:
            pbar.update(100)
            print("\n\n搞定~\n", excel_file)
        else:
            print("\n失敗")
