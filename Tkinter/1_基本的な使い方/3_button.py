import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Button practice')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0,0)
root.config(bg='red')

# ボタンの作成
button_1 = tkinter.Button(root, text='ボタン1')
# 描画(gridだと場所を指定可能)
button_1.grid(row=0, column=0)

# ボタンの位置を変更
button_2 = tkinter.Button(root, text='ボタン2')
button_2.grid(row=0, column=1)

# ボタンが押されたときに色を変える
button_3 = tkinter.Button(root, text='ボタン3', bg='pink', activebackground='yellow')
button_3.grid(row=0, column=2, padx=10, pady=10, ipadx=10, ipady=10)

# columnspanで3つのcolumnを一つとしてみる
# sticky='W'で左詰め、'E'で右詰め、'WE'で引き延ばす
button_4 = tkinter.Button(root, text='ボタン4', borderwidth=5) # 枠線を太くする
button_4.grid(row=1, column=0, columnspan=3, sticky='WE')

# 以下のようにすることで、配置を整えることができるが大変 ⇒ フレームを使用する
button_5 = tkinter.Button(root, text='test')
button_6 = tkinter.Button(root, text='test')
button_7 = tkinter.Button(root, text='test')
button_8 = tkinter.Button(root, text='test')
button_9 = tkinter.Button(root, text='test')
button_10 = tkinter.Button(root, text='test')

button_5.grid(row=2, column=0, padx=5, pady=5)
button_6.grid(row=2, column=1, padx=5, pady=5)
button_7.grid(row=2, column=2, padx=5, pady=5, sticky='w') # 3列目だけ幅が異なるので左に詰める
button_8.grid(row=3, column=0, padx=5, pady=5)
button_9.grid(row=3, column=1, padx=5, pady=5)
button_10.grid(row=3, column=2, padx=5, pady=5, sticky='w') # 3列目だけ幅が異なるので左に詰める

# ウィンドウのループ処理
root.mainloop()