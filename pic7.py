
# pip install requests
# pip install beautifulsoup4
# pip install pandas
# pip install --upgrade pandas
# pip install html5lib

import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime, timedelta
from requests.exceptions import ConnectionError

# 定義日期範圍
start_date = datetime(2007, 1, 1)
end_date = datetime(2023, 12, 30)

# 定義股票代碼範圍
start_stock_no = 1
end_stock_no = 9999

# 創建一個空的 DataFrame 用於存儲數據
result_df = pd.DataFrame()

# 循環遍歷日期範圍
current_date = start_date
while current_date <= end_date:
    # 循環遍歷股票代碼範圍
    current_stock_no = start_stock_no
    while current_stock_no <= end_stock_no:
        # 構建動態的URL
        date_str = current_date.strftime("%Y%m%d")
        stock_no_str = f"{current_stock_no:04d}"
        url = f"https://www.twse.com.tw/rwd/zh/afterTrading/STOCK_DAY_AVG?date={date_str}&stockNo={stock_no_str}&response=html"

        # 重試機制
        max_retries = 3
        for attempt in range(max_retries):
            try:
                response = requests.get(url)
                response.raise_for_status()  # 檢查是否有錯誤
                break  # 如果成功，跳出迴圈
            except ConnectionError as e:
                if attempt < max_retries - 1:
                    print(f"重試中，次數: {attempt + 1}")
                else:
                    print(f"重試失敗，達到最大次數。錯誤訊息: {e}")
                    # 在這裡您可以選擇是繼續下一次迴圈或者進行其他處理
                    continue

        # 使用BeautifulSoup解析HTML內容
        soup = BeautifulSoup(response.text, 'html.parser')

        # 找到表格內容，假設數據在第一個表格中
        table = soup.find('table')

        # 使用pandas的read_html函數將表格轉換為DataFrame
        df = pd.read_html(str(table))[0]

        # 添加日期和股票代碼列
        df['Date'] = current_date
        df['Stock Code'] = current_stock_no

        # 將當前 DataFrame 附加到結果 DataFrame
        result_df = pd.concat([result_df, df], ignore_index=True)

        # 增加股票代碼
        current_stock_no += 1

    # 增加日期
    current_date += timedelta(days=1)

# 將結果 DataFrame 保存到 Excel 文件
result_df.to_excel('output.xlsx', index=False)
