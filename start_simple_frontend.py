import http.server
import socketserver
import webbrowser
import threading
import time
import os

# 设置端口号
PORT = 8000

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 更改工作目录到当前脚本所在目录
os.chdir(current_dir)

# 创建请求处理器
Handler = http.server.SimpleHTTPRequestHandler

# 设置服务器 - 使用正确的参数
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"\n篮球鞋推荐系统前端服务器启动成功！")
    print(f"服务器运行在: http://localhost:{PORT}/simple_frontend.html")
    print("\n请在浏览器中打开以上链接访问系统")
    print("如果浏览器没有自动打开，请手动复制链接到浏览器")
    print("\n按 Ctrl+C 停止服务器")
    
    # 在新线程中打开浏览器
    def open_browser():
        time.sleep(1)  # 给服务器一点启动时间
        webbrowser.open(f"http://localhost:{PORT}/simple_frontend.html")
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # 启动服务器
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n服务器已停止")
        httpd.server_close()