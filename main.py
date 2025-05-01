import os
import src.utils
import time
import pyautogui
import threading
import keyboard

from src.heads import Point, LogLevel
from src.utils import Utils

running = False

def start_function():
    global running
    if not running:
        running = True
        Utils.log("Starting function...", LogLevel.INFO)
        # 使用线程防止阻塞主线程
        rob = src.utils.Rob()
        threading.Thread(target=rob.start).start()

def stop_function():
    global running
    if running:  # 仅在函数运行时停止
        running = False
        print("Stopping function...")


if __name__ == "__main__":

    keyboard.add_hotkey('ctrl+s', start_function)  # 启动函数的热键
    keyboard.add_hotkey('ctrl+h', stop_function)    # 停止函数的热键
    print("Press Ctrl+S to start the function and Ctrl+H to stop it...")
    keyboard.wait()  # 等待事件
    