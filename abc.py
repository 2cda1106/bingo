import random
import tkinter as tk
from tkinter import messagebox

class Bing:
    def __init__(self, x):
        self.x = x
        self.x.title("ビンゴ司会")
        self.x.config(bg="orange")  # ウィンドウの背景色を設定
        
        self.number = list(range(1, 76))  # 1から75までの番号をリストに格納
        self.selected_number = []  # 選ばれた番号の履歴を保存
        
        # ボタンのスタイルを変更
        self.select_button = tk.Button(
            x, 
            text="番号を選ぶ", 
            command=self.select_number,
            bg="lightblue",  # 背景色を水色に
            fg="black",      # テキスト色を黒に
            font=("Helvetica", 16, "bold"),  # フォントスタイルを太字に
            width=20,        # ボタンの幅
            height=3,        # ボタンの高さ
            relief="raised",  # ボタンの形状を立体的に
            borderwidth=5    # ボタンの境界線の幅
        )
        self.select_button.pack(pady=20)
        
        # ラベルのスタイルを変更
        self.number_label = tk.Label(
            x, 
            text="", 
            font=("Helvetica", 48, "bold"),  # フォントを太字に
            bg="yellow",  # 背景色を黄色に
            fg="red"      # テキスト色を赤に
        )
        self.number_label.pack(pady=20)

        # 履歴表示用ラベルのスタイルを変更
        self.history_label = tk.Label(x, text="履歴:", font=("Helvetica", 25))
        self.history_label.pack(pady=10)

    def select_number(self):
        if len(self.number) == 0:
            messagebox.showinfo("ゲーム終了", "すべての番号が選ばれました！")
            return
        
        selected = random.choice(self.number)  # 利用可能な番号からランダムに選択
        self.number.remove(selected)  # 選ばれた番号をリストから削除
        self.selected_number.append(selected)  # 選ばれた番号を履歴に追加

        # 選ばれた番号を表示
        self.number_label.config(text=str(selected))

        # 履歴を更新
        self.history_label.config(text="履歴: " + ", ".join(map(str, self.selected_number)))

if __name__ == "__main__":
    x = tk.Tk()
    bingo_system = Bing(x)
    x.mainloop()