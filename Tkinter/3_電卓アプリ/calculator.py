import tkinter
from tkinter import RIGHT

# ウィンドウの作成
root = tkinter.Tk()
root.title('電卓アプリ')
root.iconbitmap('icon.ico')
root.geometry('325x415')
root.resizable(0, 0)

# 色とフォントの設定
screen_font = ('Segoe UI', 30, 'bold')
button_font = ('Segoe UI', 20, 'bold')
light_orange = '#FFEFD5'
light_gray = '#DCDCDC'
orange = '#FFA500'

# フレームの作成
screen_frame = tkinter.LabelFrame(root)
button_frame = tkinter.LabelFrame(root)
screen_frame.pack(padx=2, pady=(5,0)) # padxで横側の空白を設定 
button_frame.pack()

# エントリーの作成
screen = tkinter.Entry(screen_frame, width=40, font=screen_font, bg=light_orange, justify=RIGHT, borderwidth=5) # justifyで右寄せ
screen.pack()

# ボタンの作成
clear_button = tkinter.Button(button_frame, text="C", font=button_font, bg=light_gray)
negate_button = tkinter.Button(button_frame, text="+/-", font=button_font, bg=light_gray)
percentage_button = tkinter.Button(button_frame, text="%", font=button_font, bg=light_gray)
divide_button = tkinter.Button(button_frame, text="÷", font=button_font, bg=orange)
seven_button = tkinter.Button(button_frame, text="7", font=button_font, bg='black', fg='white')
eight_button = tkinter.Button(button_frame, text="8", font=button_font, bg='black', fg='white')
nine_button = tkinter.Button(button_frame, text="9", font=button_font, bg='black', fg='white')
multiply_button = tkinter.Button(button_frame, text="×", font=button_font, bg=orange)
four_button = tkinter.Button(button_frame, text="4", font=button_font, bg='black', fg='white')
five_button = tkinter.Button(button_frame, text="5", font=button_font, bg='black', fg='white')
six_button = tkinter.Button(button_frame, text="6", font=button_font, bg='black', fg='white')
substract_button = tkinter.Button(button_frame, text="-", font=button_font, bg=orange)
one_button = tkinter.Button(button_frame, text="1", font=button_font, bg='black', fg='white')
two_button = tkinter.Button(button_frame, text="2", font=button_font, bg='black', fg='white')
three_button = tkinter.Button(button_frame, text="3", font=button_font, bg='black', fg='white')
add_button = tkinter.Button(button_frame, text="+", font=button_font, bg=orange)
zero_button = tkinter.Button(button_frame, text="0", font=button_font, bg='black', fg='white')
decimal_button = tkinter.Button(button_frame, text=".", font=button_font, bg='black', fg='white')
equal_button = tkinter.Button(button_frame, text="=", font=button_font, bg=orange)

# 1行目の配置
# sticky='WE'ですべての行が一番大きい幅に合わせてくれる
clear_button.grid(row=0, column=0, sticky='WE', pady=1)
negate_button.grid(row=0, column=1, sticky='WE', pady=1)
percentage_button.grid(row=0, column=2, sticky='WE', pady=1)
divide_button.grid(row=0, column=3, sticky='WE', pady=1)
# 2行目の配置
seven_button.grid(row=1, column=0, sticky='WE', ipadx=20, pady=1)
eight_button.grid(row=1, column=1, sticky='WE', ipadx=20, pady=1)
nine_button.grid(row=1, column=2, sticky='WE', ipadx=20, pady=1)
multiply_button.grid(row=1, column=3, sticky='WE', ipadx=20, pady=1)
# 3行目の配置
four_button.grid(row=2, column=0, sticky='WE', pady=1)
five_button.grid(row=2, column=1, sticky='WE', pady=1)
six_button.grid(row=2, column=2, sticky='WE', pady=1)
substract_button.grid(row=2, column=3, sticky='WE', pady=1)
# 4行目の配置
one_button.grid(row=3, column=0, sticky='WE', pady=1)
two_button.grid(row=3, column=1, sticky='WE', pady=1)
three_button.grid(row=3, column=2, sticky='WE', pady=1)
add_button.grid(row=3, column=3, sticky='WE', pady=1)
# 5行目の配置
zero_button.grid(row=4, column=0, sticky='WE', columnspan=2, pady=1)
decimal_button.grid(row=4, column=2, sticky='WE', pady=1)
equal_button.grid(row=4, column=3, sticky='WE', pady=1)


# ウィンドウのループ処理
root.mainloop()