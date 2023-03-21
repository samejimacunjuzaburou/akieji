# -*- coding: utf-8 -*-

import tkinter as tk
import asyncio
import threading
import queue
import kukei
import kanshi
import time
import subprocess


class MyApplication:
    def __init__(self, master):
        self.master = master
        self.canvas = tk.Canvas(self.master, width=300, height=200)
        self.canvas.pack()

        # ボタンを作成し、Canvasに配置する
        self.button_text = tk.StringVar()
        self.button_text.set("敵船監視")
        self.button = tk.Button(self.canvas, textvariable=self.button_text, command=self.toggle_kukei)
        self.canvas.create_window(150, 100, window=self.button)

        self.is_kukei_running = False
        self.kukei_thread = None
        self.kukei_queue = queue.Queue()

    async def kukei_loop(self):
        app = kukei.kukeiStart()

        while self.is_kukei_running:
            if kanshi.poll(app[0], app[1], app[2], app[3]):
                print("検知")
                self.is_kukei_running = False
                self.button_text.set("敵船監視")
                
            else:
                print("実行中")
                print(self.is_kukei_running)
                time.sleep(3)
                print(self.is_kukei_running)

    def start_kukei(self):
        self.is_kukei_running = True
        self.kukei_thread = threading.Thread(target=self.kukei_thread_loop)
        self.kukei_thread.start()
        self.button_text.set("■")

    def stop_kukei(self):
        self.is_kukei_running = False
        self.button_text.set("敵船監視")

    def kukei_thread_loop(self):
        asyncio.set_event_loop(asyncio.new_event_loop())
        loop = asyncio.get_event_loop()
        loop.create_task(self.kukei_loop())
        loop.run_until_complete(self.kukei_done())

    async def kukei_done(self):
        self.kukei_queue.put(None)
        subprocess.run(["./send/sendDiscord.exe"])

    def toggle_kukei(self):
        if self.is_kukei_running:
            self.stop_kukei()
            self.kukei_queue.get()
            self.kukei_thread.join()
        else:
            self.start_kukei()

root = tk.Tk()
app = MyApplication(root)
root.mainloop()