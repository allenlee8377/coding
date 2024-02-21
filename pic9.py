#舊版本的goodinfo抓檔
import os
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# 指定下载目录
download_path = "C:\\K"  # 请将路径替换为您希望保存文件的目录

# 指定 stock_list.txt 的路径
stock_list_path = "C:\\K\\stock_list.txt"

# 从文本文件中读取股票代码
with open(stock_list_path, "r") as file:
    stock_ids = [line.strip() for line in file]

# 设置 ChromeOptions
chrome_options = webdriver.ChromeOptions()

# 设置下载路径和关闭下载提示
prefs = {"download.default_directory": download_path, "download.prompt_for_download": False}
chrome_options.add_experimental_option("prefs", prefs)

# 初始化 Chrome 浏览器时传入 ChromeOptions
driver = webdriver.Chrome(options=chrome_options)

# 遍历股票清单
for stock_id in stock_ids:
    # 构建 URL
    url = f"https://goodinfo.tw/tw/ShowK_Chart.asp?STOCK_ID={stock_id}&CHT_CAT2=WEEK&PRICE_ADJ=F&SCROLL2Y=267"

    driver.get(url)

    # 使用 WebDriverWait 确保元素可见，然后点击
    period_select = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="selK_ChartPeriod"]')))

    # 使用 Select 类来处理下拉框
    select = Select(period_select)

    # 通过索引、值或可见文本选择下拉框中的选项
    # 示例：选择第二个选项，索引从 0 开始
    select.select_by_index(1)

    # 等待一段时间确保页面加载完成，根据实际情况调整等待时间
    time.sleep(30)

    # 使用提供的新 XPath 定位按钮并点击
    chart_button = driver.find_element("xpath", '//*[@id="divK_ChartDetail"]/table/tbody/tr/td/table/tbody/tr/td[2]/input[2]')
    chart_button.click()

    # 等待一段时间确保生成的 HTML 内容加载完成
    time.sleep(30)
    # 获取生成的 HTML 内容
    html_content_after_click = driver.page_source

    # 在下载目录中查找以 "K_Chart" 开头且以 ".html" 结尾的文件
    for file in os.listdir(download_path):
        if file.startswith("K_Chart") and file.endswith(".html"):
            # 构建新的文件名，使用 STOCK_ID 作为文件名
            new_file_name = f"{stock_id}_chart_data.html"
            # 构建完整文件路径
            old_file_path = os.path.join(download_path, file)
            new_file_path = os.path.join(download_path, new_file_name)
            # 重命名文件
            os.rename(old_file_path, new_file_path)
            print(f"文件已重命名为: {new_file_name}")
            break

    print(f"文件已保存为: {new_file_name}")

# 关闭浏览器
driver.quit()
