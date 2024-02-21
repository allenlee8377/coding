#保留，合併檔案用

import os

def merge_html_files(input_folder):
    # 获取输入文件夹中所有文件
    files = os.listdir(input_folder)
    
    # 用于存储文件前缀和对应的文件列表的字典
    file_dict = {}

    # 遍历所有文件
    for file in files:
        if file.endswith(".html"):
            # 提取文件名中的前缀（四位数字）
            file_prefix = file.split("_")[0]
            
            # 将文件添加到字典中对应的列表中
            if file_prefix in file_dict:
                file_dict[file_prefix].append(file)
            else:
                file_dict[file_prefix] = [file]
    
    # 遍历字典中的文件列表，将同一前缀的文件合并为一个文件
    for prefix, file_list in file_dict.items():
        merged_file_name = f"{prefix}_10y.html"
        merged_file_path = os.path.join(input_folder, merged_file_name)
        
        with open(merged_file_path, 'w', encoding='utf-8') as merged_file:
            for file in file_list:
                file_path = os.path.join(input_folder, file)
                with open(file_path, 'r', encoding='utf-8') as html_file:
                    merged_file.write(html_file.read())
        
        print(f"已合并文件: {merged_file_name}")

# Example usage:
input_folder = "C:\\K"  # 替换为您的输入文件夹路径
merge_html_files(input_folder)
