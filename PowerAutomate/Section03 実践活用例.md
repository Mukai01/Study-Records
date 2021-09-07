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