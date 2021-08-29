Option Explicit

' セルに値を入力する
Sub 入力()
    Range("A1").Value = 7
    Range("A2").Value = "月予定表"
    Range("A3").Value = #7/1/2020#
    Range("A4:A5").Formula = "=$A$1+1"
End Sub

' セルの値、書式を消去する
Sub 消去()
    Range("A1").ClearContents ' 値の消去
    Range("A2").ClearFormats ' 書式の消去
    Range("A3").Clear ' 値と書式の消去
End Sub

' セルに連続データを入力する
' 引数typeを指定すると、コピーの細かい指定が可能
Sub 連続入力()
    Range("A1") = 1
    Range("A2") = 2
    Range("A1:A2").AutoFill Range("A1:A5")
End Sub

' フォントを変更する
Sub フォント()
    Range("A1").Font.Name = "Arial Black"
    Range("A1").Font.Size = 20
    Range("A1").Font.Bold = True
    Range("A1").Font.Italic = True
    Range("A1").Font.Underline = True
    Range("A1").HorizontalAlignment = xlRight
    Range("A1").VerticalAlignment = xlBottom
End Sub

' セルの結合を設定する
Sub 結合()
    Range("A1:A3").MergeCells = True ' 結合
    Range("A1:A3").MergeCells = False ' 結合解除
End Sub

' 色の変更
' カラーパレットの左から何個目かを指定するのがThemeColor
' 上から0,0.8,0.6,0.4,-0.25,-0.5　と指定するのがTintAndShade
Sub 色()
    Range("A1:A2").Interior.ThemeColor = xlThemeColorAccent5 ' テーマの色の指定
    Range("A1").Interior.TintAndShade = 0.6 ' 色の明るさを指定
    Range("A3").Interior.Color = RGB(0, 0, 255) ' RGBで指定
    Range("A4").Interior.ColorIndex = 36 ' 色番号で指定
    Range("A1").Font.Color = vbWhite ' 文字の色を指定
End Sub

' 罫線を設定
' Linestyleで線種の指定
' Weightで太さを指定
Sub 罫線()
    Range("B2:B4").Borders.LineStyle = xlNone ' 罫線解除
    Range("C2:C4").Borders.LineStyle = xlContinuous ' 実線
    Range("E2:G4").BorderAround Weight:=xlThick  '周辺に太線
    Range("B6").Borders(xlDiagonalDown).LineStyle = xlContinuous '斜線
End Sub

' 表示形式を設定
Sub 表示形式の設定()
    Range("A1:A10").Value = 7000
    Range("A1").NumberFormatLocal = "0000" ' 4桁表示
    Range("A2").NumberFormatLocal = "#,##0" ' 桁区切り
    Range("A3").NumberFormatLocal = "0.0%" ' %表記
    Range("A4").NumberFormatLocal = "m月d日"
    Range("A5").NumberFormatLocal = "G/標準" ' 標準に戻す
End Sub

' セルの移動、コピー、形式を選択して貼り付け
Sub セルの編集()
    Worksheets(2).Select ' 2番目のワークシートを選択
    Range("B2").Select ' B2セルの選択
    
    Range("A1:A10").Value = 7
    Range("A1").Cut Range("B1") ' セルを移動
    Range("A2").Copy Range("B2") ' セルをコピー
    
    Range("A3").Copy 'コピー
    ActiveSheet.Paste Range("B3") ' クリップボードからアクティブシートに貼り付け
    
    ' 形式を選択して貼り付けるときはPasteSpecial
    Range("B4").PasteSpecial xlPasteFormats ' 書式のコピー
    
    'コピーモードの解除（セルの周りが点線で囲まれた状態）
    Application.CutCopyMode = False
End Sub

' セルの大きさの変更
Sub セルサイズ()
    Range("A1").ColumnWidth = 16
    Range("B:C").ColumnWidth = 5
    Range("A1").RowHeight = 30
    
    ' 自動調整はAutofit
    Range("A2:C5").Columns.AutoFit
End Sub


' 行・列の挿入、削除
Sub 行と列()
    Columns("B").Insert
    Rows(2).Insert CopyOrigin:=xlFormatFromRightOrBelow ' 2行目に挿入し、下のセルの書式をコピーする
    
    Columns(7).Delete ' 7行目を削除
End Sub


' フィルター
' <> 100 : 100に等しくない
' *山* : 山を含む
' ??山 : 2文字+山
Sub フィルター()
    Worksheets(3).Select ' Sheet3に移動
    
    ' xlor や xlandで組み合わせ可能
    Range("A1").AutoFilter Field:=3, Criteria1:="test", Operator:=xlOr, Criteria2:="test1"
    Range("A1").AutoFilter Field:=4, Criteria1:=">=10000"
    
    ' フィルターを削除
    Range("A1").AutoFilter Field:=3 ' 3列目のフィルターのみ解除
    ' ActiveSheet.AutoFilterMode = False ' フィルターすべて解除
End Sub

' 並び変え
Sub ソート()
    Worksheets(3).Select ' Sheet3に移動
    
    ' A1を含む表において、D1列で降順で並び替え
    ' Header で先頭行を見出しに設定
    Range("A1").Sort Key1:=Range("D1"), Order1:=xlDescending, Header:=xlYes
    
End Sub

' ウインドウ枠の固定
Sub ウインドウ枠の固定()
    Range("A2").Select
    ActiveWindow.FreezePanes = True ' 選択したセルで固定
End Sub

' ワークシートを操作する
Sub ワークシート()
    ' ワークシートの選択
    Worksheets("Sheet2").Select
    Worksheets("Sheet3").Select False ' 複数選択に加える
    
    ' シート名の変更
    Worksheets(1).Name = "集計"
    
    ' ワークシートの数を数える
    Range("A1").Value = Worksheets.Count
    
    ' ワークシートの移動、コピー
    ' 3番目の後にコピー
    Worksheets("集計").Copy After:=Worksheets(3) ' Moveを使えば移動
    ActiveSheet.Name = "集計その2"
    
    ' ワークシートの追加/削除
    Worksheets.Add Before:=Worksheets(1) ' 追加
    
    Application.DisplayAlerts = False ' 警告を表示しないようにする
    Worksheets(1).Delete
    Application.DisplayAlerts = True ' 警告の設定をもとに戻す
    
End Sub

' ワークブックを操作
Sub ワークブック()
    Workbooks("8.Property.xlsm").Activate ' アクティブ化
    
    MsgBox Workbooks(1).Path & Workbooks(1).Name ' パスとファイル名を取得

    ' 新規ワークブック作成
    Workbooks.Add
    
    ' 名前を付けて保存
    ActiveWorkbook.SaveAs ("test.xlsx")
    
    ' 上書き保存
    ActiveWorkbook.Save
    
    ' ブックを閉じる
    ActiveWorkbook.Close False ' 変更を保存せずに閉じる
    
    ' ブックを開く
    Workbooks.Open "test.xlsx"
End Sub

' ワークブックを選択して開く
' GetOpenFilename はファイルパスを取得するだけなので、そのあと開く必要がある
Sub ワークブック選択()
    ' variantは全ての型を格納可能
    Dim フォームブック名 As Variant
    Dim フォームブック As Workbook
    
    ' ワークブックのパスに移動
    ChDir ThisWorkbook.Path
    
    ' ファイルを開く画面を表示する
    フォームブック名 = Application.GetOpenFilename("エクセルファイル(*.xlsx),*.xlsx", , "エクセルファイル.xlsxの選択")
    If フォームブック名 = False Then
        MsgBox "処理を中止します"
        Exit Sub
    End If
    MsgBox フォームブック名
    
    Set フォームブック = Workbooks.Open(フォームブック名)
    MsgBox フォームブック.Worksheets.Count
End Sub

' ワークブックに名前を付けて保存する
' GetSaveAsFilename　はファイルパスを取得するだけなので、そのあと保存する必要がある
Sub ワークブック保存()
    Dim 保存ファイル名 As Variant
    ChDir ThisWorkbook.Path
    保存ファイル名 = Application.GetSaveAsFilename("既定ファイル名", "エクセルファイル(*.xlsx),*.xlsx")
    
    If 保存ファイル名 = False Then
        MsgBox "保存は中止されました"
    Else
        MsgBox 保存ファイル名
        ' ThisWorkbook.SaveAs 保存ファイル名　' 保存するには以下を実行する
    End If
End Sub


' マクロの結合
Sub マクロ1()
    マクロ2 (3)
End Sub

Sub マクロ2(番号 As Long)
    MsgBox 番号
End Sub
