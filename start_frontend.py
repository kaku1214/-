import sys
import os
import webbrowser
import subprocess
import time
import threading
import sys

# 定义项目路径
project_path = os.path.dirname(os.path.abspath(__file__))

# 定义HTTP服务器端口
port = 8000

# 启动HTTP服务器的函数
def start_server():
    try:
        # 在当前目录启动HTTP服务器
        server_process = subprocess.Popen(
            [sys.executable, '-m', 'http.server', str(port)],
            cwd=project_path,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        return server_process
    except Exception as e:
        print(f"启动服务器失败: {e}")
        return None

# 打开浏览器的函数
def open_browser():
    # 等待服务器启动
    time.sleep(1)
    # 构建URL
    url = f"http://localhost:{port}"
    # 打开浏览器
    try:
        webbrowser.open(url)
        print(f"浏览器已打开: {url}")
    except Exception as e:
        print(f"打开浏览器失败，请手动访问: {url}")

# 主函数
def main():
    print(f"正在启动篮球鞋推荐系统 (端口: {port})...")
    print("✨ 新功能：系统现已支持代码输入和流程展示")
    print("💡 有效访问代码示例：1234, 5678, 9999, 0000")
    
    # 启动服务器
    server_process = start_server()
    if not server_process:
        print("无法启动服务器，程序退出。")
        return
    
    # 直接打开浏览器（无需等待用户输入）
    open_browser()
    
    try:
        # 保持程序运行，直到用户按Enter键退出
        print("\n系统已成功启动并打开浏览器！")
        print("按Enter键可以停止服务器...")
        print("📌 请点击导航栏的'输入代码'按钮体验新功能")
        input()
    except KeyboardInterrupt:
        print("正在停止服务器...")
    finally:
        # 终止服务器进程
        if server_process.poll() is None:
            server_process.terminate()
            server_process.wait(timeout=3)
    
    print("服务器已停止。")

if __name__ == "__main__":
    main()