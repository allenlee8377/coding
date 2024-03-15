#最後整理完的excel合併成一份且只有一個分頁，且有檔案來源名稱

import os
import pandas as pd
from tqdm import tqdm

# 要合併的Excel檔案所在的資料夾路徑
folder_path = r'C:\Users\allenlee\Desktop\DBtest\excel_all'

# 獲取資料夾中所有的Excel檔案路徑
excel_files = [os.path.join(folder_path, file) for file in os.listdir(folder_path) if file.endswith('.xlsx')]

# 建立一個空的DataFrame來儲存合併後的資料
merged_data = pd.DataFrame()

# 使用 tqdm 顯示進度條
for file in tqdm(excel_files, desc="合併中"):
    # 讀取Excel檔案
    excel_data = pd.read_excel(file, sheet_name=None)
    
    # 將各個分頁的資料合併到一個DataFrame中
    for sheet_name, df in excel_data.items():
        # 移除重複的橫列資料
        df.drop_duplicates(inplace=True)
        
        # 將原始分頁名稱加上檔案名稱前綴以區分來源，不包含副檔名
        df['Source_File'] = os.path.splitext(os.path.basename(file))[0]
        merged_data = pd.concat([merged_data, df], ignore_index=True)

# 將合併後的資料寫入新的Excel檔案
merged_file_path = os.path.join(folder_path, 'merged_data.xlsx')
merged_data.to_excel(merged_file_path, index=False)

print("資料已成功合併並寫入到", merged_file_path)
