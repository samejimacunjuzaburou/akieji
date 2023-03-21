import tkinter as tk

class DragRect:
    def __init__(self, master):
        self.master = master
        self.rect = None
        self.start_x = None
        self.start_y = None
        self.end_x = None
        self.end_y = None
        
        # キャンバスの作成
        self.canvas = tk.Canvas(self.master, bg="white", highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<B1-Motion>", self.on_move_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)

    def on_button_press(self, event):
        # ドラッグ開始時の座標を取得
        self.start_x = event.x_root
        self.start_y = event.y_root
        
        # 矩形を作成
        self.rect = self.canvas.create_rectangle(self.start_x, self.start_y, self.start_x, self.start_y, outline="black", width=2)

    def on_move_press(self, event):
        # 現在の座標を取得し、矩形を更新
        self.end_x = event.x_root
        self.end_y = event.y_root
        self.canvas.coords(self.rect, self.start_x, self.start_y, self.end_x, self.end_y)

    def on_button_release(self, event):
        # ドラッグ終了時の座標を取得
        self.end_x = event.x_root
        self.end_y = event.y_root

        # キャンバスを閉じる
        self.master.destroy()

def kukeiStart():
    root = tk.Tk()
    root.attributes("-fullscreen", True) # フルスクリーン表示
    root.attributes("-topmost", True) # 常に最前面に表示
    root.attributes("-alpha",0.5) # キャンバスの背景を半透明にする

    # ウィンドウサイズを画面サイズに設定
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    root.geometry("{}x{}".format(screen_width, screen_height))

    app = DragRect(root)
    root.mainloop()

    return app.start_x, app.start_y, app.end_x, app.end_y
