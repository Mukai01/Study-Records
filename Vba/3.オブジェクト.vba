Option Explicit
'【基礎】
Sub with文()
    ' 1つめのワークシートに対して、処理を実行
    With Worksheets(1).Range("B2")
        .Font.Bold = True
        .HorizontalAlignment = xlCenter
    End With
End Sub


' オブジェクトを変数に入れる場合はsetを使う
Sub オブジェクト変数()
    Dim ws集計 As Worksheet
    Set ws集計 = ThisWorkbook.Worksheets(1)
    With ws集計.Range("B2")
        .Font.Bold = False
    End With
End Sub

' 選択されているオブジェクトの取得には以下がある
' Selection : 選択されているオブジェクト
' ActiveCell : 選択されている単一のセル
' ActiveSheet : 最前面にあるワークシート
' ActiveWorkbook : 最前面にあるブック
' Thisworkbook : コードの保存先のブック


' オフセットプロパティ
Sub オフセット()
    Range("A1").Offset(1, 3).Select
End Sub

' Resizeプロパティ
Sub リサイズ()
    Range("B1").Resize(3, 4).Select
End Sub

' CurrentRegionプロパティ
Sub Region()
    Range("B1").CurrentRegion.Select
    MsgBox Range("B1").CurrentRegion.Rows.Count
End Sub


' 【アドバンス】
' 表の見出し行以外を選択
Sub 見出し以外選択()
    Dim 行数 As Long
    Dim 列数 As Long
    行数 = Range("B1").CurrentRegion.Rows.Count
    列数 = Range("B1").CurrentRegion.Columns.Count
    
    Range("B1").Offset(1).Resize(行数 - 1, 列数).Select
    
End Sub


' 【アドバンス】
' ctrl + ↓で、一番下の行に移動
Sub 一番下の行に移動()
    MsgBox Range("B1").End(xlDown).Row
    MsgBox Cells(Rows.Count, 2).End(xlUp).Row ' 空白とかがある場合は、一番下に行った後、ctrl↑を押す
End Sub
