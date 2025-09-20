import os

# 文件路径
file_path = 'index.html'

# 尝试不同的编码方式读取文件
def read_file_with_encoding(file_path):
    encodings = ['utf-8', 'gbk', 'cp936', 'gb2312', 'latin-1']
    
    for encoding in encodings:
        try:
            with open(file_path, 'r', encoding=encoding) as f:
                content = f.read()
                print(f"成功使用{encoding}编码读取文件")
                return content, encoding
        except UnicodeDecodeError:
            continue
    
    # 如果所有编码都失败，使用二进制模式读取
    with open(file_path, 'rb') as f:
        content = f.read()
        print("使用二进制模式读取文件")
        return content, 'binary'

# 读取文件
content, encoding = read_file_with_encoding(file_path)

# 定义要查找和替换的内容
search_text = "            // 初始化步骤显示\n       python -m http.server 8000python -m http.server 8000     showStep(1);"
replace_text = "            // 初始化步骤显示\n            showStep(1);"

# 执行替换
if encoding == 'binary':
    # 如果是二进制模式，将搜索和替换文本转换为字节
    search_bytes = search_text.encode('utf-8')
    replace_bytes = replace_text.encode('utf-8')
    
    if search_bytes in content:
        new_content = content.replace(search_bytes, replace_bytes)
        with open(file_path, 'wb') as f:
            f.write(new_content)
        print("已成功修复JavaScript错误（二进制模式）！")
    else:
        print("未找到需要修复的错误代码。")
else:
    # 如果是文本模式
    if search_text in content:
        new_content = content.replace(search_text, replace_text)
        with open(file_path, 'w', encoding=encoding) as f:
            f.write(new_content)
        print("已成功修复JavaScript错误！")
    else:
        print("未找到需要修复的错误代码。")