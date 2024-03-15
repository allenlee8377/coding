import pandas as pd
import os

# 读取id.txt文件中的四位数
with open(r'C:\Users\allenlee\Desktop\DBtest\html_A\id.txt', 'r') as f:
    ids = f.read().splitlines()

# 创建一个空字典用于存储每个四位数对应的DataFrame
dfs_dict = {}

# 遍历每个四位数
for id_number in ids:
    # 构建文件路径
    file_A_path = rf'C:\Users\allenlee\Desktop\DBtest\html_A\{id_number}_chart_data_1.xlsx'
    file_B_path = rf'C:\Users\allenlee\Desktop\DBtest\html_A\{id_number}_chart_data_2.xlsx'

    # 检查文件是否存在
    if os.path.exists(file_A_path) and os.path.exists(file_B_path):
        # 读取文件到DataFrame中
        df_A = pd.read_excel(file_A_path)
        df_B = pd.read_excel(file_B_path)

        # 将_2的内容接在_1的后面
        merged_df = pd.concat([df_A, df_B], ignore_index=True)

        # 移除重复行
        merged_df = merged_df.drop_duplicates()

        # 将合并后的DataFrame存储到字典中
        dfs_dict[id_number] = merged_df

# 创建一个Excel writer对象
output_folder = r'C:\Users\allenlee\Desktop\DBtest\html_A\combined_files'
os.makedirs(output_folder, exist_ok=True)

for id_number, df in dfs_dict.items():
    # 构建输出文件路径
    output_path = os.path.join(output_folder, f'new_{id_number}.xlsx')

    # 写入到Excel文件中
    writer = pd.ExcelWriter(output_path, engine='xlsxwriter')
    df.to_excel(writer, sheet_name=id_number, index=False)
    writer.close()
