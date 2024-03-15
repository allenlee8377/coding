import os
import requests

# 设置共同的网址部分和下载目录
#base_url = "https://www.twse.com.tw/staticFiles/inspection/inspection/02/003/"
#base_url = "https://www.twse.com.tw/staticFiles/inspection/inspection/07/031/"
#https://www.twse.com.tw/staticFiles/inspection/inspection/01/003/202301_C01003.zip
#https://www.twse.com.tw/staticFiles/inspection/inspection/01/003/202306_C01003.zip
base_url = "https://www.twse.com.tw/staticFiles/inspection/inspection/01/003/"
download_dir = r"C:\Users\allenlee\Desktop\DDD"

# 创建下载目录
os.makedirs(download_dir, exist_ok=True)

# 循环遍历年份和月份，下载文件
for year in range(2014, 2024):
    for month in range(1, 13):
        # 构造文件名
        filename = f"{year}{month:02d}_C01003.zip"
        #filename = f"{year}_C07031.zip"
        url = base_url + filename
        filepath = os.path.join(download_dir, filename)
        
        # 下载文件
        try:
            response = requests.get(url)
            with open(filepath, "wb") as file:
                file.write(response.content)
            print(f"下载成功: {filepath}")
        except Exception as e:
            print(f"下载失败: {filepath}, 错误信息: {str(e)}")

#投資人類別交易比重統計表
#https://www.twse.com.tw/staticFiles/inspection/inspection/07/031/2023_C07031.zip
#https://www.twse.com.tw/staticFiles/inspection/inspection/07/031/2022_C07031.zip