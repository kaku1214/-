import os

# 读取index.html文件
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'index.html')

# 以二进制模式读取文件
with open(file_path, 'rb') as file:
    content = file.read()

# 修复JavaScript错误
# 查找并替换错误的代码行（使用二进制字符串）
error_text = b'python -m http.server 8000python -m http.server 8000     showStep(1);'
fixed_text = b'showStep(1);'
new_content = content.replace(error_text, fixed_text)

# 以二进制模式保存修复后的文件
with open(file_path, 'wb') as file:
    file.write(new_content)

print("已成功修复index.html文件中的JavaScript错误！")
print(f"替换了: '{error_text.decode('utf-8', errors='replace')}'")
print(f"替换为: '{fixed_text.decode('utf-8')}'")