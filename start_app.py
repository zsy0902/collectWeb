import os
import subprocess
import webbrowser
import time

def start_django_server():
    # 启动 Django 开发服务器
    subprocess.Popen(['python', 'manage.py', 'runserver','0.0.0.0:8000'])

def open_browser():
    # 等待 Django 服务器启动
    time.sleep(5)
    # 打开浏览器并指向 Django 服务器地址
    webbrowser.open('http://127.0.0.1:8000/')

if __name__ == '__main__':
    start_django_server()
    open_browser()
