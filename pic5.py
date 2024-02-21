import docx
import pandas as pd
import re

def convert_word_to_excel_with_pandas(word_file, excel_file):
    # 读取 Word 文档
    doc = docx.Document(word_file)

    # 初始化一个空的 DataFrame
    df = pd.DataFrame(columns=['Content'])

    # 遍历 Word 文档的段落，并逐行加入 DataFrame
    for paragraph in doc.paragraphs:
        df = df.append({'Content': paragraph.text}, ignore_index=True)

    # 将 DataFrame 写入 Excel 文件
    df.to_excel(excel_file, index=False)

    # 获取文件名并分割
    file_name = word_file.split('.')[0]
    model = file_name.split('_')[0]

    # 使用正则表达式搜寻关键字的行，并将这行到文末的内容存入 fan_table 列表
    fan_table = []
    keyword_pattern = re.compile(r'Min\s+CPU\s+MAX')
    found = False

    for index, row in df.iterrows():
        if keyword_pattern.search(row['Content']):
            found = True
            fan_table.append(row['Content'])
        elif found:
            fan_table.append(row['Content'])

    # 打印结果或进一步处理 fan_table 列表
    print(f"Model: {model}")
    print("Fan Table:")
    for row in fan_table:
        print(row)

    print(f'最終結果要取的值 機種= {model} Fan_Table參數= {fan_table[-1]}')

# 使用示例
convert_word_to_excel_with_pandas('C:\\Users\\allenlee\\Desktop\\BUND\\PWM mode\\DS2419+_fan_tabel_result_20180125.docx', 'A_output_excel_file.xlsx')