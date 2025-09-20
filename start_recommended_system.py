import http.server
import socketserver
import webbrowser
import threading
import time
import os

# 设置端口号（8000和8080可能被占用，使用8090）
PORT = 8090

# 获取当前目录
current_dir = os.path.dirname(os.path.abspath(__file__))

# 更改工作目录到当前脚本所在目录
os.chdir(current_dir)

# 创建请求处理器
Handler = http.server.SimpleHTTPRequestHandler

# 尝试停止可能已在运行的服务器（通常不需要，但为了保险起见）
httpd = None

try:
    # 创建并启动服务器
    httpd = socketserver.TCPServer(("", PORT), Handler)
    
    print(f"\n🏀 篮球鞋推荐系统已成功启动！🏀")
    print(f"🌐 服务器运行在: http://localhost:{PORT}/index.html")
    print("\n🎯 系统功能更新：")
    print("✨ 新增代码输入功能 - 在导航栏点击'输入代码'按钮")
    print("📊 新增系统流程展示 - 输入代码后查看完整流程")
    print("🔧 修复了JavaScript错误 - 系统运行更加稳定")
    print("\n💡 有效访问代码示例：1234, 5678, 9999, 0000")
    print("\n📌 使用指南：")
    print("1. 在浏览器中打开上述链接")
    print("2. 点击导航栏右侧的'输入代码'按钮")
    print("3. 输入任意有效代码，查看系统流程")
    print("4. 开始您的篮球鞋个性化测评之旅")
    print("\n🛑 按 Ctrl+C 停止服务器")
    
    # 在新线程中打开浏览器
    def open_browser():
        time.sleep(1)  # 给服务器一点启动时间
        webbrowser.open(f"http://localhost:{PORT}/index.html")
    
    browser_thread = threading.Thread(target=open_browser)
    browser_thread.daemon = True
    browser_thread.start()
    
    # 启动服务器
    httpd.serve_forever()
except KeyboardInterrupt:
    print("\n🛑 服务器已停止")
finally:
    if httpd:
        httpd.server_close()

print("\n感谢使用篮球鞋推荐系统！")