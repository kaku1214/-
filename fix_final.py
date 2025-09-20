# 这个脚本用于修复index.html中的JavaScript错误
# 错误: JavaScript代码中包含了错误的服务器命令文本

# 以二进制模式读取文件，避免编码问题
with open('index.html', 'rb') as f:
    content = f.read()

# 定义要查找和替换的模式
# 注意：这里需要处理空格和换行符
search_patterns = [
    b'python -m http.server 8000python -m http.server 8000     showStep(1);',
    b'python -m http.server 8000 python -m http.server 8000     showStep(1);',
    b'python -m http.server 8000\npython -m http.server 8000     showStep(1);'
]
replace_with = b'showStep(1);'

# 尝试所有可能的模式
fixed = False
for pattern in search_patterns:
    if pattern in content:
        content = content.replace(pattern, replace_with)
        fixed = True
        print(f"已找到并修复错误模式: {pattern}")
        break

# 如果没有找到，尝试更宽泛的匹配
if not fixed:
    if b'python -m http.server 8000' in content:
        # 找到所有出现的位置并统计
        count = content.count(b'python -m http.server 8000')
        print(f"发现{count}个'python -m http.server 8000'实例")
        
        # 只移除JavaScript初始化部分的错误文本
        # 查找"// 初始化步骤显示"后面的内容
        init_step_pos = content.find(b'// 初始化步骤显示')
        if init_step_pos != -1:
            # 找到showStep(1);的位置
            show_step_pos = content.find(b'showStep(1);')
            if show_step_pos != -1 and show_step_pos > init_step_pos:
                # 构建修复后的内容
                before = content[:init_step_pos + len(b'// 初始化步骤显示')]
                after = content[show_step_pos:]
                content = before + b'\n            ' + after
                fixed = True
                print("已成功修复JavaScript初始化步骤错误！")

# 保存修复后的文件
with open('index.html', 'wb') as f:
    f.write(content)

if fixed:
    print("index.html文件已成功修复！")
else:
    print("未能自动修复错误，请尝试手动编辑文件。")