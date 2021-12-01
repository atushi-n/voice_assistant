import threading
import tkinter as tk
from multiprocessing import Process

import yamaarasi


class MainFrame(tk.Frame):


    def __init__(self, title, size, master):#継承するんじゃなかった。　pythonのうざさをくらった
        super().__init__(master)#スーパクラスのコンストラクタ

        self.startup = True

        self.pack()

        master.title(title) #tkのインスタンスフィールド
        master.geometry(size)

        self.assistant = yamaarasi.Assistant()
        self.th = threading.Thread(target=self.assistant.listen)

        #生成
        self.textbox = tk.Entry(master=master)
        self.run_button = tk.Button(master, text="run", command=self.run_click)
        self.stop_button = tk.Button(master, text="stop", command=self.stop_click)

        #配置
        self.textbox.place(relx=0.0, rely=0.2, relwidth=1, relheight=0.1)
        self.run_button.place(relx=0.0, rely=0.1, relwidth=0.5, relheight=0.1)
        self.stop_button.place(relx=0.5, rely=0.1, relwidth=0.5, relheight=0.1)


    def run_click(self):

        if self.startup:#初回はスレッドを起動
            self.startup = False
            self.th.start()

        #初回よりあとはスレッドの再開を行う　eventをsetすることでwaitをすり抜ける
        self.textbox.delete(0, tk.END)
        self.textbox.insert(0, "listen")
        self.assistant.event.set()

    def stop_click(self):

        #eventをclearすることでwaitに止められる
        self.textbox.delete(0, tk.END)
        self.textbox.insert(0, "holiday")
        self.assistant.event.clear()




