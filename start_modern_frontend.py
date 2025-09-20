#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
篮球鞋推荐系统 - 现代前端启动脚本
此脚本用于启动HTTP服务器，方便用户访问modern_frontend.html页面
"""

import http.server
import socketserver
import webbrowser
import threading
import time
import os
import sys
from pathlib import Path

# 设置端口号
PORT = 8001

# 获取当前工作目录
CURRENT_DIR = Path(os.path.dirname(os.path.abspath(__file__)))

# 设置前端文件路径
FRONTEND_FILE = "modern_frontend.html"
FRONTEND_PATH = CURRENT_DIR / FRONTEND_FILE

class SimpleHTTPRequestHandlerWithIndex(http.server.SimpleHTTPRequestHandler):
    """自定义HTTP请求处理器，当访问根目录时自动重定向到现代前端文件"""
    
    def do_GET(self):
        """处理GET请求"""
        if self.path == '/':
            self.path = f'/{FRONTEND_FILE}'
        
        try:
            return super().do_GET()
        except Exception as e:
            self.send_error(404, f"文件未找到: {self.path}")
            print(f"错误: {e}")

    def log_message(self, format, *args):
        """自定义日志输出，仅显示重要信息"""
        if any(x in args for x in ('GET', '404')):
            return
        print(f"[服务器日志] {format % args}")


def open_browser():
    """在浏览器中打开前端页面"""
    time.sleep(1)  # 等待服务器启动
    url = f"http://localhost:{PORT}"
    print(f"\n正在打开浏览器访问: {url}")
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"无法自动打开浏览器: {e}")
        print(f"请手动在浏览器中访问: {url}")


def start_server():
    """启动HTTP服务器"""
    handler = SimpleHTTPRequestHandlerWithIndex
    
    try:
        # 创建TCP服务器
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print(f"\n===== 篮球鞋推荐系统 - 现代前端 =====")
            print(f"运行在端口: {PORT}")
            print(f"当前目录: {CURRENT_DIR}")
            print(f"前端文件: {FRONTEND_FILE}")
            print(f"访问地址: http://localhost:{PORT}")
            print("==================================")
            print("\n按 Ctrl+C 停止服务器...")
            
            # 在浏览器中打开页面
            browser_thread = threading.Thread(target=open_browser)
            browser_thread.daemon = True
            browser_thread.start()
            
            # 启动服务器
            httpd.serve_forever()
    except OSError as e:
        if "address already in use" in str(e):
            print(f"错误: 端口 {PORT} 已被占用！")
            print("请关闭占用该端口的程序，或者使用以下命令手动启动服务器：")
            print(f"python -m http.server {PORT}")
            print(f"然后在浏览器中访问: http://localhost:{PORT}/{FRONTEND_FILE}")
        else:
            print(f"启动服务器时发生错误: {e}")
    except KeyboardInterrupt:
        print("\n服务器已停止")
    except Exception as e:
        print(f"发生未知错误: {e}")


def check_file_exists():
    """检查前端文件是否存在"""
    global FRONTEND_FILE, FRONTEND_PATH
    
    if not FRONTEND_PATH.exists():
        print(f"错误: 前端文件 '{FRONTEND_FILE}' 未找到！")
        print(f"请确保在 '{CURRENT_DIR}' 目录下存在该文件")
        
        # 尝试查找其他前端文件
        html_files = list(CURRENT_DIR.glob("*.html"))
        if html_files:
            print("\n在当前目录找到以下HTML文件:")
            for i, file in enumerate(html_files, 1):
                print(f"{i}. {file.name}")
            
            try:
                choice = input("请选择要使用的HTML文件编号 (输入q退出): ")
                if choice.lower() == 'q':
                    return False
                
                index = int(choice) - 1
                if 0 <= index < len(html_files):
                    FRONTEND_FILE = html_files[index].name
                    FRONTEND_PATH = CURRENT_DIR / FRONTEND_FILE
                    print(f"已选择文件: {FRONTEND_FILE}")
                    return True
                else:
                    print("无效的选择")
                    return False
            except ValueError:
                print("输入无效")
                return False
        else:
            print("当前目录下没有找到任何HTML文件")
            return False
    return True


def print_welcome():
    """打印欢迎信息"""
    welcome_msg = """
    欢迎使用 篮球鞋推荐系统 - 现代前端启动器
    =======================================================
    此脚本将启动一个本地HTTP服务器，并在浏览器中打开篮球鞋推荐系统的现代前端界面。
    
    系统特点：
    - 现代化UI设计，支持响应式布局
    - 四步测评流程，准确匹配用户需求
    - 智能推荐算法，基于打球风格和偏好
    - 多语言支持（中文、英文、日文）
    - 丰富的交互效果和动态元素
    =======================================================
    """
    print(welcome_msg)


def main():
    """主函数"""
    print_welcome()
    
    # 检查前端文件是否存在
    if not check_file_exists():
        print("程序无法继续执行，退出。")
        sys.exit(1)
    
    # 启动服务器
    start_server()


if __name__ == "__main__":
    main()