import tkinter
from tkinter.constants import END

def print_text():
    # entry_1に入力した文字をラベルとして作成する
    text = tkinter.Label(frame_2, text=entry_1.get())
    text.pack()
    # 入力欄の削除
    entry_1.delete(0, END) # 0-最後の文字まで削除

def count(number):
    # 関数外でも使用できるようにglobalで宣言する
    global value
    text = tkinter.Label(frame_2, text=number, bg='#499499')
    text.pack()
    value = number+1

# ウィンドウの作成
root = tkinter.Tk()
root.title('Entry practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# frameの作成
frame_1 = tkinter.Frame(root, bg='green', width=500, height=200)
frame_2 = tkinter.Frame(root, bg='pink', width=500, height=300)
frame_1.pack(padx=10, pady=10)
frame_2.pack(padx=10, pady=(0,10))

# エントリーの作成
entry_1 = tkinter.Entry(frame_1, width=30)
entry_1.grid(row=0, column=0, padx=5, pady=5)

# エントリーの大きさにframeの大きさが依存する関係を0にする
frame_1.grid_propagate(0)
# ラベルを作るときにpack()を使うのでpack_propagate()を使用する
frame_2.pack_propagate(0)

# ボタンを作成
button_1 = tkinter.Button(frame_1, text='出力', command=print_text) # ボタンを押すとprint_textを実行させる
button_1.grid(row=0, column=1, padx=5, pady=5)

# 引数を渡して関数を実行
value = 0
button_2 = tkinter.Button(frame_1, text='カウント', command=lambda:count(value))
button_2.grid(row=1, column=0, columnspan=2, padx=5, pady=5, sticky='WE')

# ウィンドウのループ処理
root.mainloop()