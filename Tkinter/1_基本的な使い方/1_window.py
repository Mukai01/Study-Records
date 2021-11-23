import tkinter

# ウィンドウの作成
root = tkinter.Tk()

# タイトルを設定
root.title('Window Practice!')

# アイコンを設定
root.iconbitmap('icon.ico')

# ウィンドウのサイズを設定
root.geometry('300x800')
root.resizable(0, 1) # 横方向のサイズの変更を0とする（禁止）

# 色を設定
root.config(bg='red')

# サブウィンドウの作成
sub_window = tkinter.Toplevel()
sub_window.title('Second Window')
sub_window.config(bg='#123123')
sub_window.geometry('200x300+500+500') # +500で右に500、次の500が下に500移動させる

# ウィンドウのループ処理
# これが無いとウィンドウが消えてしまう
root.mainloop()

