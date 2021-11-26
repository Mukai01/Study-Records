import tkinter

# ウィンドウの作成
root = tkinter.Tk()
root.title('Menu Practice!')
root.geometry('260x200')
root.resizable(0, 0)

# 関数の作成
def open_setting():
    subwindow = tkinter.Toplevel()
    subwindow.title('設定')
    subwindow.geometry('200x100')
    subwindow_label = tkinter.Label(subwindow, text='設定画面です')
    subwindow_label.pack()

# メニューバーの作成
# メニューバーの親となるコンテナの作成
menubar = tkinter.Menu(root)
# メニューバーをルートに固定
root.config(menu=menubar)

# 設定メニューの作成
setting_menu = tkinter.Menu(menubar, tearoff=0) # tearoff=0で切り取り線が消える
menubar.add_cascade(label='設定', menu=setting_menu)

# ファイルメニューの作成
file_menu = tkinter.Menu(menubar, tearoff=0)
menubar.add_cascade(label='ファイル', menu=file_menu)

# プルダウンメニューを追加
setting_menu.add_command(label='環境設定', command=open_setting)
setting_menu.add_command(label='終了')
file_menu.add_command(label='新規ファイル')

# ボタンの作成
button_1 = tkinter.Button(root, text='テスト')
button_1.grid(row=0, column=0, padx=70, ipadx=10)

# ループ処理
root.mainloop()