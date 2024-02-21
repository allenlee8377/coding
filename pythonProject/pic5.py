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
    word_table = []
    result_table = []
    fan_table = []
    keyword_pattern = re.compile(r'Min\s+CPU\s+MAX')
    found = False

    for index, row in df.iterrows():
        if keyword_pattern.search(row['Content']):
            found = True
            word_table.append(row['Content'])
        elif found:
            word_table.append(row['Content'])

    print(word_table)

    # 打印结果或进一步处理 fan_table 列表
    print(f"Model: {model}")

    list_range = len(word_table)
    for i in range(1, list_range):
        list_value = list(filter(None, word_table[i].split()))
        result_table.append(list_value)
    # Initialize an empty list to store indices
    indices = []
    # Iterate through the outer list
    for sublist in result_table:
        # Check if the sublist has the required indices and values
        if len(sublist) > 2 and sublist[0] == 'Min' and sublist[1] == 'CPU' and sublist[2] == 'MAX':
            # Append the index of the sublist to the 'indices' list
            indices.append(result_table.index(sublist))

    # Print the result
    print("查出 'Min', 'CPU', 'MAX' 的index位置，並要將它轉成一個整數才能用", indices)
    start_index = int(indices[0])
    print(f'start_index= {start_index}, 型態是: {type(start_index)}')

    # +1 是因為要去掉 title 'Min', 'CPU', 'MAX'，迴圈範圍從 頭 到 尾，重新存一份 list
    for i in range(int(start_index) + 1, len(result_table)):
        fan_table.append(result_table[i])

    print(f'fan_table整份清單= {fan_table}')
    print(f'第一組資料: {fan_table[0]}')
    print(f'最後一組資料: {fan_table[-1]}')


# 使用示例
convert_word_to_excel_with_pandas('DS1520+ _fan_table_result_20200219.docx', 'output_excel_file.xlsx')