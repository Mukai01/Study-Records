import tkinter
from PIL import ImageTk, Image

# ウィンドウの作成
root = tkinter.Tk()
root.title('Image practice!')
root.iconbitmap('icon.ico')
root.geometry('550x550')
root.resizable(0, 0)

# 画像の配置
# PhotoImageではpngしか使えない
image_1 = tkinter.PhotoImage(file='dice.png')
label_1 = tkinter.Label(root, image=image_1)
label_1.pack()

# ボタンとして表示
button_1 = tkinter.Button(root, image=image_1)
button_1.pack()

# jpg画像を使う場合はこちら
image_by_pillow = ImageTk.PhotoImage(Image.open('mountain.jpg'))
label_by_pillow = tkinter.Label(root, image=image_by_pillow)
label_by_pillow.pack()

# もし関数を使う場合はグローバル変数として宣言が必要
def display_image():
    global image_by_pillow
    image_by_pillow = ImageTk.PhotoImage(Image.open('mountain.jpg'))
    label_by_pillow = tkinter.Label(root, image=image_by_pillow)
    label_by_pillow.pack()

# ウィンドウのループ処理
root.mainloop()