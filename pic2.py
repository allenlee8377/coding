from docx import Document
import os

def search_word_in_docx(docx_path, target_word):
    doc = Document(docx_path)

    found_paragraphs = []

    for paragraph in doc.paragraphs:
        if target_word in paragraph.text:
            found_paragraphs.append(paragraph.text)

    return found_paragraphs

# 让用户分别输入Word文档路径和文档名称
docx_directory = input("请输入Word文档所在文件夹路径：")
docx_filename = input("请输入Word文档文件名：")
docx_path = os.path.join(docx_directory, f'{docx_filename}'+".docx")
print(docx_path)

target_word = input("请输入要查找的目标字符串：")

# 搜索指定字符串
result = search_word_in_docx(docx_path, target_word)

# 打印搜索结果
if result:
    for idx, paragraph in enumerate(result, 1):
        print(f"匹配 {idx}: {paragraph}")
else:
    print("未找到匹配的内容。")



