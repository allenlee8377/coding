# build.py
# pip install pyinstaller

# build.py

import PyInstaller.__main__

options = [
    '--onefile',        # 打包成单个可执行文件
    '--noconsole',      # 不显示控制台窗口
    '--hidden-import', 'selenium',    # 隐藏 selenium 模块
    'pic11.py'   # 要打包的 Python 脚本文件名
]

PyInstaller.__main__.run(options)
