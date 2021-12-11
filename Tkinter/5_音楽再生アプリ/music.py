import tkinter
import tkinter.filedialog
from tkinter import END, ANCHOR
import pygame.mixer as pymix

# ウィンドウの作成
root = tkinter.Tk()
root.title('音楽再生アプリ')
root.iconbitmap('icon.ico')
root.geometry('500x600')
root.resizable(0, 0)

# フォントの定義
basic_font = ('Times New Roman', 12)
list_font = ('Times New Roman', 15)

# 関数の作成
def add_item():
    file_type = [('','*')] # 全てのファイルを指定
    file_name = tkinter.filedialog.askopenfilename(filetypes=file_type, initialdir='./')

    my_listbox.insert(END, file_name)

def remove_item():
    my_listbox.delete(ANCHOR) # 選択した物を削除

def clear_list():
    my_listbox.delete(0, END) # 全て削除

def play():
    # 音量を別の関数で変えるために、globalで宣言
    global music_player
    # 既に流れている音楽を終了する
    pymix.quit()

    # ファイルパスを取得
    n = my_listbox.curselection() # 何番目かを取得
    sound_file = my_listbox.get(n)
    # 音楽再生
    pymix.init() # 初期化が必要
    sounds = pymix.Sound(sound_file)
    music_player = sounds.play()
    music_player.set_volume(0.1) # 0.01刻みで 0.00-1.00 まで選択可能

def stop():
    pymix.pause()

def restart():
    pymix.unpause()

# adjust_volumeはラムダ関数を使わなくても、volumeを渡せる
def adjust_volume(volume):
    music_player.set_volume(float(volume))

# フレームの作成
input_frame = tkinter.Frame(root)
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
vol_frame = tkinter.Frame(root)
input_frame.pack()
output_frame.pack()
button_frame.pack()
vol_frame.pack()

# ファイルに関するボタンを作成
list_add_button = tkinter.Button(input_frame, text='追加', borderwidth=2, font=basic_font, command=add_item)
list_remove_button = tkinter.Button(input_frame, text='選択削除', borderwidth=2, font=basic_font, command=remove_item)
list_clear_button = tkinter.Button(input_frame, text='一括削除', borderwidth=2, font=basic_font, command=clear_list)
list_add_button.grid(row=0, column=0, padx=2, pady=15, ipadx=5)
list_remove_button.grid(row=0, column=1, padx=2, pady=15, ipadx=5)
list_clear_button.grid(row=0, column=2, padx=2, pady=15, ipadx=5)

# スクロールバーの追加
my_scrollbar = tkinter.Scrollbar(output_frame)

# 音楽リストの作成
my_listbox = tkinter.Listbox(output_frame, width=45, height=15, yscrollcommand=my_scrollbar.set, borderwidth=3, font=list_font) # スクロールバーを定義
my_listbox.grid(row=0, column=0)

# スクロールバーとリストボックスの紐づけ
my_scrollbar.config(command=my_listbox.yview)
my_scrollbar.grid(row=0, column=1, sticky='NS') # North/South で上下に引き延ばす

# 音楽再生に関するボタン作成
play_button = tkinter.Button(button_frame, text='再生', borderwidth=2, font=basic_font, command=play)
stop_button = tkinter.Button(button_frame, text='一時停止', borderwidth=2, font=basic_font, command=stop)
restart_button = tkinter.Button(button_frame, text='再開', borderwidth=2, font=basic_font, command=restart)
play_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
stop_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
restart_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)

# 音量バーの作成
vol_label = tkinter.Label(vol_frame, text='音量')
vol_scale = tkinter.Scale(vol_frame, orient='horizontal', length=300, from_=0.0, to=1.0, resolution=0.01, showvalue=0, command=adjust_volume) # horizontal:横方向, showvalue=0:数字が見えなくなる
# 初期値を設定
vol_scale.set(0.1)
# 描画
vol_label.grid(row=0, column=0, padx=10)
vol_scale.grid(row=0, column=1, padx=10)

# ループ処理の実行
root.mainloop()