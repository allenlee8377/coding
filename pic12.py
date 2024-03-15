#重新填合併後excel檔案

import os
import pandas as pd

# 指定待處理的檔案路徑位置
folder_path = 'C:\\Users\\allenlee\\Desktop\\DBtest\\excel_all'

# 遍歷指定目錄下的所有檔案
for file_name in os.listdir(folder_path):
    # 構建完整的檔案路徑
    file_path = os.path.join(folder_path, file_name)
    
    # 檢查是否為檔案
    if os.path.isfile(file_path) and file_name.endswith('.xlsx'):
        # 讀取原始Excel文件
        xls = pd.ExcelFile(file_path)

        # 創建新的Excel文件
        output_folder = 'C:\\Users\\allenlee\\Desktop\\DBtest\\excel_all'
        
        # 取得舊檔案名稱的前四位
        new_file_name = 'new_' + file_name[:4] + '.xlsx'
        output_file = os.path.join(output_folder, new_file_name)
        
        writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

        # 處理每個 Excel 檔案
        for sheet_name in xls.sheet_names:
            # 檢查分頁名稱是否與檔名前四位數相同
            if sheet_name[:4] == file_name[:4]:
                # 讀取指定分頁的資料
                df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=0)
                
                # 移除空白或重複的橫列內容
                df = df.drop_duplicates().dropna()

                # 將處理後的資料寫入新的 Excel 文件中
                df.to_excel(writer, index=False, sheet_name=sheet_name)

        # 保存並關閉文件寫入器
        writer.close()

        # Print 生成文件的名稱
        print("新的Excel文件已經成功生成：", output_file)


'''
import os
import pandas as pd

# 指定原始Excel文件的路徑
file_path = 'C:\\Users\\allenlee\\Desktop\\DBtest\\com\\output_with_10y.xlsx'

# 讀取原始Excel文件
xls = pd.ExcelFile(file_path)

# 創建新的Excel文件
output_folder = 'C:\\Users\\allenlee\\Desktop\\DBtest\\com'
output_file = os.path.join(output_folder, 'new_output_with_10y.xlsx')
writer = pd.ExcelWriter(output_file, engine='xlsxwriter')

# 處理每個分頁
for sheet_name in xls.sheet_names:
    # 讀取每個分頁的資料，從第3列開始
    df = pd.read_excel(file_path, sheet_name=sheet_name, skiprows=0)
    
    # 移除空白或重複的橫列內容
    df = df.drop_duplicates().dropna()

    # 將每個分頁的資料寫入新的Excel文件中
    df.to_excel(writer, index=False, sheet_name=sheet_name)

# 保存並關閉文件寫入器
writer.close()

print("新的Excel文件已經成功生成：", output_file)
'''