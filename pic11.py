#SOP-1
#新版的goodinfo的抓檔

import os
import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import datetime

def merge_html_files(stock_id, download_path):
    merged_file_name = f"{stock_id}_10y.html"
    merged_file_path = os.path.join(download_path, merged_file_name)

    with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
        for suffix in ["_1", "_2"]:
            file_name = f"{stock_id}_chart_data{suffix}.html"
            file_path = os.path.join(download_path, file_name)
            with open(file_path, 'r', encoding='utf-8') as html_file:
                merged_file.write(html_file.read())

    print(f"合并后的HTML文件已保存为: {merged_file_name}")

def main():
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

    # 新的元素ID
    new_element_id1 = 'edtSTART_DT'
    new_element_id2 = 'edtEND_DT'

    # 获取当前年份
    current_year = datetime.datetime.now().year

    # 遍历股票清单
    for stock_id in stock_ids:
        # 初始化结束年份为当前年份的前一年
        end_year = current_year - 1

        for i in range(2):  # 执行两次以获取10年的数据
            # 构建URL
            url = f"https://goodinfo.tw/tw/ShowK_Chart.asp?STOCK_ID={stock_id}&CHT_CAT=WEEK&PRICE_ADJ=T"
            driver.get(url)


            try:
                # 使用WebDriverWait等待元素出现
                element1 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, new_element_id1)))
                element2 = WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.ID, new_element_id2)))

                # 构造开始日期和结束日期
                start_year = end_year - 4
                start_date = f"00{start_year}0101"  # 开始日期往前推五年
                end_date = f"00{end_year}1231"

                # 在输入框中填写内容
                element1.clear()  # 清空输入框中的内容
                element1.send_keys(start_date)  # 填写开始日期
                element2.clear()  # 清空输入框中的内容
                element2.send_keys(end_date)  # 填写结束日期

                # 随机等待一段时间，模拟真实用户操作
                time.sleep(random.randint(3, 5))

                # 点击查询按钮
                query_button = driver.find_element(By.XPATH, '//*[@value="查詢"]')
                query_button.click()

                # 等待一段时间确保页面加载完成，根据实际情况调整等待时间
                time.sleep(random.randint(5, 10))

                # 模拟滚动页面，向下滚动到页面底部
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

                # 随机等待一段时间，模拟真实用户操作
                time.sleep(random.randint(3, 5))

                # 再次点击下载按钮
                download_button = driver.find_element(By.XPATH, '//*[@id="divK_ChartDetail"]/table/tbody/tr/td/table/tbody/tr/td[3]/nobr/input[2]')
                download_button.click()

                # 随机等待一段时间确保下载完成，根据实际情况调整等待时间
                time.sleep(random.randint(10, 20))

                # 文件命名后缀，根据循环次数确定
                suffix = f"_{i + 1}"

                # 在下载目录中查找以 "K_Chart" 开头且以 ".html" 结尾的文件
                for file in os.listdir(download_path):
                    if file.startswith("K_Chart") and file.endswith(".html"):
                        # 构建新的文件名，使用 STOCK_ID 作为文件名
                        new_file_name = f"{stock_id}_chart_data{suffix}.html"
                        # 构建完整文件路径
                        old_file_path = os.path.join(download_path, file)
                        new_file_path = os.path.join(download_path, new_file_name)
                        # 重命名文件
                        os.rename(old_file_path, new_file_path)
                        print(f"文件已重命名为: {new_file_name}")
                        break

                print(f"文件已保存为: {new_file_name}")

            except TimeoutException:
                print(f"股票代碼 {stock_id} 的元素定位超时，请检查页面结构是否变更。")
                continue

            # 循环结束后更新结束年份为当前开始年份的前一年，准备下一次循环
            end_year = start_year - 1

    # 关闭浏览器
    driver.quit()

    # 合并HTML文件
    for stock_id in stock_ids:
        merge_html_files(stock_id, download_path)

if __name__ == "__main__":
    main()
