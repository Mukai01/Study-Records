import tkinter
from tkinter import END

# 関数を定義
def submit_name():
    if radio_value.get() == 'morning':
        output_text = 'おはようございます!'+name.get()+'さん'
        greeting_label = tkinter.Label(output_frame, text=output_text, bg=output_color)
    elif radio_value.get() == 'noon':
        output_text = 'こんにちは!'+name.get()+'さん'
        greeting_label = tkinter.Label(output_frame, text=output_text, bg=output_color)
    elif radio_value.get() == 'night':
        output_text = 'こんばんは!'+name.get()+'さん'
        greeting_label = tkinter.Label(output_frame, text=output_text, bg=output_color)
    
    greeting_label.pack()
    
    # 入力文字列の削除
    name.delete(0, END)

# ウィンドウの作成
root = tkinter.Tk()
root.title('挨拶アプリ')
root.iconbitmap('icon.ico')
root.geometry('400x400')
root.resizable(0, 0)

# 色の定義
output_color = "#A9A9A9"

# Frameの作成
input_frame = tkinter.Frame(root)
output_frame = tkinter.LabelFrame(root, bg=output_color) # LabelFrameは枠線つき
input_frame.pack(pady=10)
output_frame.pack(fill='both', expand=True, padx=10, pady=(0,10)) # 縦にも引き延ばす際にはexpandを設定する

# ボタン画像の読み込み
submit_img = tkinter.PhotoImage(file="submit.PNG")
# jpegの場合
# from PIL import ImageTk
# submit_img = ImageTk.PhotoImage(Image.open('icon.png'))

# エントリー&ボタンの作成
name = tkinter.Entry(input_frame, width=30)
name.insert(0, '名前を入力してください') # 0文字目から文章を表示
submit_button = tkinter.Button(input_frame, image=submit_img, command=submit_name)
name.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
submit_button.grid(row=0, column=3, padx=10, pady=10)

# ラジオボタンの作成
radio_value = tkinter.StringVar()
radio_value.set('morning')

morning_button = tkinter.Radiobutton(input_frame, text='朝', variable=radio_value, value='morning')
noon_button = tkinter.Radiobutton(input_frame, text='昼', variable=radio_value, value='noon')
night_button = tkinter.Radiobutton(input_frame, text='夜', variable=radio_value, value='night')
morning_button.grid(row=1, column=0)
noon_button.grid(row=1, column=1)
night_button.grid(row=1, column=2)

# ウィンドウのループ処理
root.mainloop()