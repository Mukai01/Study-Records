import tkinter
from tkinter import ttk
from googletrans import Translator
# pip install googletrans==4.0.0-rc1

# 翻訳用のインスタンスを作成
translator = Translator()

# ウィンドウの作成
root = tkinter.Tk()
root.title('翻訳アプリ')
root.iconbitmap('icon.ico')
root.geometry('655x480')
root.resizable(0, 0)

# 色、フォントの設定
bg_color = '#87CEFA'
button_color = '#4672B4'
normal_font = ('Arial', 10)
bold_font = ('Arial', 10, 'bold')
root.config(bg=bg_color)

# 関数の作成
def convert():
    languages = {
        '日本語':'ja',
        '英語':'en',
        '中国語':'zh-ch',
        'フランス語':'fr',
        'ドイツ語':'de',
        'ヒンディー語':'hi',
    }

    before_text = input_box.get('1.0', 'end-1c') # 1行目0文字目から文章の終わりまで(endだけだと最後の文字+改行を取得してしまう)
    before_language = input_pulldown.get()
    after_language = output_pulldown.get()

    after_text = translator.translate(before_text, src=languages[before_language], dest=languages[after_language])

    # 表示
    output_box.insert('1.0', after_text.text)

# プルダウンの作成
language_list = ['日本語', '英語', '中国語', 'フランス語', 'ドイツ語', 'ヒンディー語']

input_pulldown = ttk.Combobox(root, value=language_list, font=normal_font, justify='center') # justifyで文字を中央揃え
output_pulldown = ttk.Combobox(root, value=language_list, font=normal_font, justify='center')
to_label = tkinter.Label(root, text='to', font=normal_font, bg=bg_color)

input_pulldown.grid(row=0, column=0, padx=10, pady=10)
to_label.grid(row=0, column=1,padx=10, pady=10)
output_pulldown.grid(row=0, column=2, padx=10, pady=10)

# 初期値
input_pulldown.set('日本語')
output_pulldown.set('英語')

# 入力、出力欄の作成
# entryだと複数行は不可
input_box = tkinter.Text(root, font=normal_font, width=40, height=20, borderwidth=3)
output_box = tkinter.Text(root, font=normal_font, width=40, height=20, borderwidth=3)
equal_sign = tkinter.Label(root, text='=', font=normal_font, bg=bg_color)

input_box.grid(row=1, column=0, padx=10, pady=10)
equal_sign.grid(row=1, column=1)
output_box.grid(row=1, column=2, padx=10, pady=10)

# 初期値
input_box.insert('1.0', '翻訳したい文章を入力') # Textの時は1行目の、0列目と指定する

# ボタンの作成
convert_button = tkinter.Button(root, text='翻訳', font=bold_font, fg='white', bg=button_color, command=convert)
save_button = tkinter.Button(root, text='保存', font=bold_font, fg='white', bg=button_color)

convert_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10, ipadx=50)
save_button.grid(row=3, column=0, columnspan=3,padx=10, pady=(0,10), ipadx=50)

# ウィンドウのループ処理
root.mainloop()