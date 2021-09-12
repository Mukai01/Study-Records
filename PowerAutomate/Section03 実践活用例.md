# 選択したフォルダ内のファイルを連番にする
* メッセージボックス: フォルダーの選択ダイアログを表示
* フォルダ: フォルダー内のファイルを取得
* ファイル: ファイルの名前を変更する
    * 複数ファイルを一括処理可能

```
Display.SelectFolder Description: $'''フォルダーの選択''' InitialDirectory: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section3 実践活用\\img''' IsTopMost: True SelectedFolder=> SelectedFolder ButtonPressed=> ButtonPressed
Folder.GetFiles Folder: SelectedFolder FileFilter: $'''*.PNG''' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> Files
File.OverwriteWithSequentialSuffix Files: Files SequenceNewName: $'''写真''' SequencePosition: File.AddTextPosition.AfterName StartNumberingAt: 1 IncrementBy: 1 SequenceSeparator: File.Separator.Underscore UsePadding: True Padding: 3 IfFileExists: File.IfExists.DoNothing RenamedFiles=> RenamedFiles
```

# 選択したフォルダ内のPDFを結合する
* メッセージボックス: フォルダーの選択ダイアログを表示
* フォルダ: フォルダー内のファイルを取得
    * ファイルを降順に並べ替える
* メッセージボックス: 入力ダイアログを表示
* PDF: PDFファイルを統合

```
Display.SelectFolder Description: $'''フォルダ選択''' InitialDirectory: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section3 実践活用\\pdf''' IsTopMost: False SelectedFolder=> SelectedFolder ButtonPressed=> ButtonPressed
Folder.GetFiles Folder: SelectedFolder FileFilter: $'''*.pdf''' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: True SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> Files
Display.InputDialog Title: $'''ファイル名有力''' Message: $'''結合後のファイル名を入力してください''' DefaultValue: $'''結合結果''' InputType: Display.InputType.SingleLine IsTopMost: False UserInput=> UserInput ButtonPressed=> ButtonPressed2
Pdf.MergeFiles PDFFiles: Files MergedPDFPath: $'''%SelectedFolder%\\%UserInput%.pdf''' IfFileExists: Pdf.IfFileExists.AddSequentialSuffix PasswordDelimiter: $''',''' MergedPDF=> MergedPDF
```

# 選択したフォルダ内のファイルを印刷する
* メッセージボックス: フォルダーの選択ダイアログを表示
* フォルダ: フォルダー内のファイルを取得
* ループ: For each
* システム: ドキュメントの印刷

```
Display.SelectFolder Description: $'''フォルダ選択''' InitialDirectory: $'''C:\\Users\\nakam\\study-records\\PowerAutomate\\data\\Section3 実践活用\\img+pdf''' IsTopMost: False SelectedFolder=> SelectedFolder ButtonPressed=> ButtonPressed
Folder.GetFiles Folder: SelectedFolder FileFilter: $'''*''' IncludeSubfolders: False FailOnAccessDenied: True SortBy1: Folder.SortBy.NoSort SortDescending1: False SortBy2: Folder.SortBy.NoSort SortDescending2: False SortBy3: Folder.SortBy.NoSort SortDescending3: False Files=> Files
LOOP FOREACH CurrentItem IN Files
    DISABLE System.PrintDocument DocumentPath: CurrentItem
    Display.ShowMessage Title: CurrentItem Message: CurrentItem Icon: Display.Icon.None Buttons: Display.Buttons.OK DefaultButton: Display.DefaultButton.Button1 IsTopMost: False ButtonPressed=> ButtonPressed2
```

# エクセル情報をWebに入力
* メッセージボックス: フォルダーの選択ダイアログを表示
* Excel: Excelの起動
* Excel: Excelワークシートから最初の空の列や行を取得
* Excel: Excelワークシートから読み取り
* ループ: For each
    * CurrenItemにExcelDataを入れる
    * CurrentItem[0]とするとテーブルの1つめを表す
* 条件: If (CurrentItem[0]がからの時ループを抜ける)
* ループ: ループを抜ける

* ループの中でWebレコーダーの内容を入れる
* Webオートメーション: ブラウザを閉じる


# Webの捜査をWebレコーダー無しで実施
* Webオートメーション: 新しいChromeを起動
* Webオートメーション: Webフォーム入力: Webページ内のテキストフィールドに入力
    * ctrl + clickで指定
* Webオートメーション: Webデータ抽出: Webページ上の要素の詳細を取得します
    * ctrl + clickで指定
* テキスト: テキストを置換する
    * 空白にする場合は%""%
* テキスト: テキストを数値に変換
* メッセージボックス: メッセージを表示