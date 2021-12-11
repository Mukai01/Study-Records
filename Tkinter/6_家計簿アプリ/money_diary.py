import tkinter
import tkinter.ttk as ttk
import csv

DATABASE_FILE = 'money_database.csv'

root = tkinter.Tk()
root.title('家計簿アプリ')
root.iconbitmap('icon.ico')
root.geometry('500x450')
root.resizable(0, 0)

# tkinterのverによってはバグでデータの色が変わらなかったりする
# その対応の為、この決まり文句を記述する
def fixed_map(option):
    return [elm for elm in style.map('Treeview', query_opt=option) if elm[:2] != ('!disabled', '!selected')]

# 関数の作成
def insert_data(row_data):
    tree.insert('', 'end', values=(row_data[0], row_data[1], row_data[2])) # 1つめの引数は階層の親を入れる, endは末尾に追加

def delete():
    # 選択したアイテムを格納(タプルで返される)
    selected_ids = tree.selection()
    for item_id in selected_ids:
        tree.delete(item_id)
    # データベースに反映する
    update_csv()

# データベースの中身をツリービューに表示する関数
def reflect_database():
    with open(DATABASE_FILE, 'r', encoding='utf-8-sig', errors='ignore') as f:
        data_list = list(csv.reader(f)) # 関数に渡すためにリスト形式にする

    for data in data_list:
        insert_data(data)

# csvを更新する関数
def update_csv():
    all_ids = tree.get_children() # 現在のツリーに表示されているidを取得
    all_data = []
    # データの読み込み
    for item_id in all_ids:
        content = list(tree.item(item_id, 'values'))
        all_data.append(content)
    # 書き込み
    with open(DATABASE_FILE, 'w', encoding='utf-8-sig', errors='ignore') as f:
        writer = csv.writer(f, lineterminator='\n')
        writer.writerows(all_data)

# ツリービューにデータを追加する関数
def add():
    add_window()
    # 編集、削除できなくする
    edit_button.config(state='disabled')
    delete_button.config(state='disabled')
    add_button.config(state='disabled')

# 追加ウィンドウを開く
def add_window():
    global date_entry, category_entry, money_entry, add_sub_window
    add_sub_window = tkinter.Toplevel()
    add_sub_window.geometry("200x200")
    add_sub_window.title('データ追加')

    date_label = tkinter.Label(add_sub_window, text='日付')
    date_entry = tkinter.Entry(add_sub_window, width=20)
    date_label.grid(row=0, column=0, padx=10, pady=20)
    date_entry.grid(row=0, column=1, padx=10, pady=20)

    category_label = tkinter.Label(add_sub_window, text='内訳')
    category_entry = tkinter.Entry(add_sub_window)
    category_label.grid(row=1, column=0, padx=10, pady=(0,20))
    category_entry.grid(row=1, column=1, padx=10, pady=(0,20))

    money_label = tkinter.Label(add_sub_window, text='金額')
    money_entry = tkinter.Entry(add_sub_window)
    money_label.grid(row=2, column=0, padx=10, pady=(0,20))
    money_entry.grid(row=2, column=1, padx=10, pady=(0,20))

    save_button = tkinter.Button(add_sub_window, text='保存', command=add_row)
    save_button.grid(row=3, column=0, columnspan=2)

# 行を追加する関数
def add_row():
    new_date = date_entry.get()
    new_category = category_entry.get()
    new_money = money_entry.get()
    new_data = [new_date, new_category, new_money]
    insert_data(new_data) # データを追加
    update_csv() # csvを更新
    add_sub_window.destroy() # ウィンドウを閉じる
    # ボタンの有効化
    edit_button.config(state='normal')
    delete_button.config(state='normal')
    add_button.config(state='normal')

# ツリービューのデータを編集する関数
def edit():
    global selected_id
    selected_id = tree.selection()[0] # 一番初めの情報を取り出す
    if len(selected_id) > 0:
        selected_data = tree.item(selected_id, 'values')
        edit_window(selected_data)
        edit_button.config(state='disabled')
        delete_button.config(state='disabled')
        add_button.config(state='disabled')

# 編集ウィンドウを作成する関数
def edit_window(selected_data):
    global date_entry, category_entry, money_entry, edit_sub_window
    edit_sub_window = tkinter.Toplevel()
    edit_sub_window.geometry('200x200')
    edit_sub_window.title('データ追加')

    date_label = tkinter.Label(edit_sub_window, text='日付')
    date_entry = tkinter.Entry(edit_sub_window, width=20)
    date_label.grid(row=0, column=0, padx=10, pady=20)
    date_entry.grid(row=0, column=1, padx=10, pady=20)
    date_entry.insert(0, selected_data[0]) # デフォルトでデータを表示

    category_label = tkinter.Label(edit_sub_window, text='内訳')
    category_entry = tkinter.Entry(edit_sub_window)
    category_label.grid(row=1, column=0, padx=10, pady=(0,20))
    category_entry.grid(row=1, column=1, padx=10, pady=(0,20))
    category_entry.insert(0, selected_data[1])

    money_label = tkinter.Label(edit_sub_window, text='金額')
    money_entry = tkinter.Entry(edit_sub_window)
    money_label.grid(row=2, column=0, padx=10, pady=(0,20))
    money_entry.grid(row=2, column=1, padx=10, pady=(0,20))
    money_entry.insert(0, selected_data[2])

    save_button = tkinter.Button(edit_sub_window, text='保存', command=edit_row)
    save_button.grid(row=3, column=0, columnspan=2)

# 行を編集する関数
def edit_row():
    # 元のデータを削除
    tree.delete(selected_id)

    new_date = date_entry.get()
    new_category = category_entry.get()
    new_money = money_entry.get()
    new_data = [new_date, new_category, new_money]
    insert_data(new_data) # データを追加
    update_csv() # csvを更新
    edit_sub_window.destroy() # ウィンドウを閉じる
    # ボタンの有効化
    edit_button.config(state='normal')
    delete_button.config(state='normal')
    add_button.config(state='normal')

# frame作成
output_frame = tkinter.Frame(root)
button_frame = tkinter.Frame(root)
output_frame.pack()
button_frame.pack()

# ツリービューの作成
tree = ttk.Treeview(output_frame)
tree['columns'] = (1, 2, 3)
tree['show'] = 'headings' # 設定したcolumnだけを表示（階層は非表示）

# カラム幅の設定
tree.column(1, width=130) # column1の幅を130
tree.column(2, width=130)
tree.column(3, width=130)

# 見出しの設定
tree.heading(1, text='日付')
tree.heading(2, text='内訳')
tree.heading(3, text='金額')

# 表スタイルの指定
style = ttk.Style()
style.configure("Treeview.Heading", font=("Arial", 12, "bold"), rowheight=100, foreground="blue")
style.configure("Treeview", font=("Arial", 8), rowheight=30)

# バグ対応処理を追加（決まり文句)
style.map('Treeview', foreground=fixed_map('foreground'), background=fixed_map('background'))

# データの追加
# tree.insert('', 'end', values=('2021/01/01', '食料品', '4600')) # 1つめの引数は階層の親を入れる, endは末尾に追加
# tree.insert('', 'end', values=('2021/01/02', '光熱費', '4600'))
# tree.insert('', 'end', values=('2021/01/03', '旅費', '4600'))
# insert_data(['2021/01/01', '食料品', '4600'])
# insert_data(['2021/01/02', '光熱費', '4600'])
# insert_data(['2021/01/03', '旅費', '4600'])

reflect_database()

# 階層構造の作成
# parent = tree.insert("", "end", values=('cccc', 'cccc', 'cccc'), text='parent_1', tags='gray') # textが階層の名前になる
# child = tree.insert(parent, "end", values=('ddd', 'ddd', 'ddd'), text='child')
# tree.insert("", "end", values=('eeee', 'eeee', 'eeee'), text='parent_2', tags='pink')

# データの装飾
# tree.tag_configure('gray', background='gray') # 第一引数はタグを表し、そのタグのデータの背景色を変える
# tree.tag_configure('pink', background='pink')

tree.pack(pady=20)

# テーブルデータ編集に関するボタン作成
add_button = tkinter.Button(button_frame, text='追加', borderwidth=2, command=add)
edit_button = tkinter.Button(button_frame, text='編集', borderwidth=2, command=edit)
delete_button = tkinter.Button(button_frame, text='削除', borderwidth=2, command=delete)
add_button.grid(row=0, column=0, padx=5, pady=15, ipadx=5)
edit_button.grid(row=0, column=1, padx=5, pady=15, ipadx=5)
delete_button.grid(row=0, column=2, padx=5, pady=15, ipadx=5)

# ループ処理
root.mainloop()