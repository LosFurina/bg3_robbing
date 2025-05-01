import os
import src.utils
import time
import pyautogui
import threading
import keyboard

from src.heads import Point, LogLevel
from src.utils import Utils

running_event = threading.Event()
worker_thread = None

def start_function():
    global worker_thread
    if not running_event.is_set():  # 仅在函数未运行时启动
        running_event.set()  # 设置事件为True
        Utils.log("Starting function...", LogLevel.INFO)
        rob = src.utils.Rob()
        # 创建并启动线程，并传递参数
        worker_thread = threading.Thread(target=rob.start, args=(running_event,))
        worker_thread.start()
        Utils.log(f"Thread started with ID: {worker_thread.ident}", LogLevel.INFO)

def stop_function():
    global worker_thread
    if running_event.is_set():  # 仅在函数运行时停止
        Utils.log("Stopping function...", LogLevel.INFO)
        running_event.clear()  # 清除事件，设置为False
        # 等待线程结束
        if worker_thread is not None:
            worker_thread.join()  # 等待线程安全地退出
            Utils.log(f"Thread with ID: {worker_thread.ident} has been stopped.", LogLevel.INFO)



if __name__ == "__main__":

    keyboard.add_hotkey('ctrl+s', start_function)  # 启动函数的热键
    keyboard.add_hotkey('ctrl+h', stop_function)    # 停止函数的热键
    print("Press Ctrl+S to start the function and Ctrl+H to stop it...")
    keyboard.wait()  # 等待事件
    