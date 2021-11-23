import tkinter
import tkinter.font as font

# ウィンドウの作成
root = tkinter.Tk()
root.title('Label Practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0,0)
root.config(bg='red')

# ラベルの作成
label_1 = tkinter.Label(root, text='よろしくお願いします')
# ラベルを描画
label_1.pack()

# ラベルのフォントを指定
label_2 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'))
label_2.pack()

# 背景色/文字色を設定
label_3 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray', fg='green')
label_3.pack(padx=10, pady=10) # 横方向と、縦方向の空白を設定

# 引数はconfigでも設定可能
label_4 = tkinter.Label(root)
label_4.config(text='よろしくお願いします')
label_4.config(bg='gray')
# pady をこうすると、上には0で下には10の空白が入る
# ipadx/ipadyはラベルの内側の空白
label_4.pack(padx=10, pady=(0, 10), ipadx=50, ipady=20, anchor='w') # anchor: w(west)で左寄せ、e(east)で右寄せ

# ラベルを引き延ばす
label_5 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray', fg='green')
label_5.pack(padx=10, pady=10, fill='x') # xで横に引き延ばす

# ラベルを縦に引き延ばす
label_6 = tkinter.Label(root, text='よろしくお願いします', font=('Arial', 10, 'bold'), bg='gray', fg='green')
label_6.pack(padx=10, pady=10, fill='y', expand=True) # 縦に引き延ばす場合はexpand=Trueが必要、fill='both'で縦横になる

# 使用できるフォントの確認
print(font.families())

# ウィンドウのループ処理
root.mainloop()