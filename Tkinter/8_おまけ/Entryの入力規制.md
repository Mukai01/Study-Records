```python
# 5文字以下を判定する関数
def limit_character(string):
    boolean_limit = len(string) <= 5
    return boolean_limit

# 5文字以上でボタンが押せるようになる
def least_character(string):
    if len(string) >= 5:
        button_1['state'] = 'normal'
    return True

# 文字数制限の検証関数
vc_1 = root.register(limit_character)
vc_2 = root.register(least_character)

# validate='key'で文字が入力されるたびにcommandを実行
# %P で入力を引数に渡す
entry_1 = tkinter.Entry(root, width=30, validate='key', validatecommand=(vc_1, '%P')) # 5文字以上入力できなくなる 
entry_2 = tkinter.Entry(root, width=30, validate='key', validatecommand=(vc_2, '%P')) # 5文字以上無いとボタンが押せなくなる
```