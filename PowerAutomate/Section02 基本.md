# 選択ダイアログを表示し、メッセージを表示

* メッセージボックス：入力ダイアログを表示
* メッセージボックス：メッセージを表示
```
Display.SelectFromList Title: $'''リストから選択''' Message: $'''Power Automateは難しいですか？''' List: $'''とても簡単
簡単な方
普通
ちょっと難しい
とても難しい''' IsTopMost: False AllowEmpty: False SelectedItem=> SelectedItem SelectedIndex=> SelectedIndex ButtonPressed=> ButtonPressed3
Display.ShowMessage Title: $'''回答の確認''' Message: $'''%SelectedItem%ですか？''' Icon: Display.Icon.None Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: False ButtonPressed=> ButtonPressed
```

# ファイルをコピーして名前を変える
* ファイル：ファイルのコピー
* ファイル：ファイルの名前を変更する

```
File.Copy Files: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section2 基本\\folder1\\test''' Destination: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section2 基本\\folder2''' IfFileExists: File.IfExists.DoNothing CopiedFiles=> CopiedFiles
File.RenameAddDateOrTime Files: CopiedFiles DateTimeToAdd: File.DateTimeToAdd.Current DateTimePosition: File.AddTextPosition.AfterName DateTimeSeparator: File.Separator.Space DateTimeFormat: $'''yyyyMMdd''' IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```


# エクセルファイルの転記
以下を使って、Excelを起動し、新しいエクセルにコピーした後、ファイル名を指定して保存する
* Excel：Excelの起動
* Excel: Excelワークシートから最初の空の列や行を取得
* Excel: Excelワークシートから読み取り
* Excel: Excelワークシートに書き込み
* メッセージボックス: 入力ダイアログを表示
* Excel: Excelの保存

```
Excel.LaunchAndOpen Path: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section2 基本\\meibo.xlsx''' Visible: True ReadOnly: False LoadAddInsAndMacros: False Instance=> ExcelInstance
Excel.GetFirstFreeColumnRow Instance: ExcelInstance FirstFreeColumn=> FirstFreeColumn FirstFreeRow=> FirstFreeRow
Excel.ReadCells Instance: ExcelInstance StartColumn: $'''A''' StartRow: 3 EndColumn: $'''B''' EndRow: FirstFreeRow - 1 ReadAsText: False FirstLineIsHeader: False RangeValue=> ExcelData
Excel.Launch Visible: True LoadAddInsAndMacros: False Instance=> ExcelInstance2
Excel.WriteCell Instance: ExcelInstance2 Value: ExcelData Column: $'''B''' Row: 1
Display.InputDialog Title: $'''ファイル名入力''' Message: $'''保存するファイル名を入力してください''' InputType: Display.InputType.SingleLine IsTopMost: False UserInput=> UserInput ButtonPressed=> ButtonPressed
Excel.SaveAs Instance: ExcelInstance2 DocumentFormat: Excel.ExcelFormat.FromExtension DocumentPath: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section2 基本\\%UserInput%'''
Excel.Close Instance: ExcelInstance
Excel.Close Instance: ExcelInstance2
```

# エクセルファイルの転記（Loop/If)
* ループ : Loop
* 条件 : If

```
Excel.LaunchAndOpen Path: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section2 基本\\meibo.xlsx''' Visible: True ReadOnly: False LoadAddInsAndMacros: False Instance=> ExcelInstance
Excel.Launch Visible: True LoadAddInsAndMacros: False Instance=> ExcelInstance2
LOOP LoopIndex FROM 3 TO 9 STEP 1
    Excel.ReadCell Instance: ExcelInstance StartColumn: $'''B''' StartRow: LoopIndex ReadAsText: False CellValue=> ExcelData
    IF ExcelData = $'''SQ''' THEN
        Excel.ReadCell Instance: ExcelInstance StartColumn: $'''A''' StartRow: LoopIndex ReadAsText: False CellValue=> ExcelData2
        Excel.GetFirstFreeColumnRow Instance: ExcelInstance2 FirstFreeColumn=> FirstFreeColumn FirstFreeRow=> FirstFreeRow
        Excel.WriteCell Instance: ExcelInstance2 Value: ExcelData2 Column: $'''A''' Row: FirstFreeRow
    END
END
```

# Webページの温度情報を取得し、CSVに書き出し

* 新しいChromeを起動: Webページ上の要素の詳細を取得

# Webレコーダー

Webレコーダーを実行

# デスクトップレコーダー

デスクトップレコーダーを実行

# フォルダによる分岐

以下を使って、フォルダーが存在しないときはメッセージを表示してフローを停止させる。
* 条件：フォルダーが存在する場合
  * フォルダーが次の場合=存在しない　とすると存在しないときの処理が書ける
* メッセージボックス：メッセージを表示
* フローコントロール：フローを停止する

```
IF (Folder.DoesNotExist Path: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section2 基本\\folder3''') THEN
    Display.ShowMessage Title: $'''エラー''' Message: $'''フォルダーが存在しません。''' Icon: Display.Icon.None Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: False ButtonPressed=> ButtonPressed
    EXIT Code: 0
END
```