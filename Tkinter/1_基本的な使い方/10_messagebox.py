import tkinter
from tkinter import messagebox

# ウィンドウの作成
root = tkinter.Tk()
root.title('Messagebox Practice!')
root.geometry('300x430')
root.resizable(0, 0)

# 関数を設定
def show_message():
    messagebox.showinfo('お知らせ', 'お知らせです')
def show_error():
    messagebox.showerror('エラー', 'エラーです')
def show_warning():
    messagebox.showwarning('警告', '警告です')
def ask_yesno():
    yesno = messagebox.askyesno('質問', 'ウィンドウを本当に閉じますか')
    print(yesno) # 返り値はBoolean
    if yesno == True:
        root.destroy() # ウィンドウを閉じる
def ask_question():
    answer = messagebox.askquestion('質問', '実行しますか')
    print(answer) # 返り値はyes/no
def ask_cancel():
    answer = messagebox.askokcancel('キャンセル', 'キャンセルしますか')
    print(answer)
def ask_retry():
    answer = messagebox.askretrycancel('リトライ', 'リトライしますか')
    print(answer)


# ボタンの作成
button_1 = tkinter.Button(root, text='お知らせ', command=show_message)
button_2 = tkinter.Button(root, text='エラー', command=show_error)
button_3 = tkinter.Button(root, text='警告', command=show_warning)
button_4 = tkinter.Button(root, text='yesno質問', command=ask_yesno)
button_5 = tkinter.Button(root, text='質問', command=ask_question)
button_6 = tkinter.Button(root, text='キャンセル質問', command=ask_cancel)
button_7 = tkinter.Button(root, text='リトライ質問', command=ask_retry)


button_1.grid(row=0, column=0, padx=100, pady=30, ipadx=10)
button_2.grid(row=1, column=0, padx=100, pady=(0, 30), ipadx=10)
button_3.grid(row=2, column=0, padx=100, pady=(0, 30), ipadx=10)
button_4.grid(row=3, column=0, padx=100, pady=(0, 30), ipadx=10)
button_5.grid(row=4, column=0, padx=100, pady=(0, 30), ipadx=10)
button_6.grid(row=5, column=0, padx=100, pady=(0, 30), ipadx=10)
button_7.grid(row=6, column=0, padx=100, pady=(0, 30), ipadx=10)


# ループ処理
root.mainloop()