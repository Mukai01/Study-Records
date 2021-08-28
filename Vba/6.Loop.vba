Option Explicit
'【基礎】
' For i = 1 To 5 Step 2 のようにStepも指定可能
Sub ループの基礎()
    Dim i As Long
    For i = 1 To 3
        MsgBox i
    Next
End Sub

'【演習】
' A-C列を3行ごとに太字にするプログラム
Sub ①三行ごとに太字設定()
    Dim i As Long
    For i = 1 To 30 Step 3
        Range(Cells(i, 1), Cells(i, 3)).Font.Bold = True
    Next
End Sub

'【アドバンス】
' For each 変数 in コレクション　でもループ可能
' ブック内のすべてのワークシートの名前を変更
Sub ワークシート名変更()
    Dim wsシート As Worksheet
    For Each wsシート In Worksheets
        wsシート.Name = "A-" & wsシート.Name
    Next
End Sub

'【アドバンス】
' 全てのブックの全てのワークシートに対して、処理を実行
Sub 全ブックワークシート名変更()
    Dim ブック As Workbook
    Dim wsシート As Worksheet
    For Each ブック In Workbooks
        For Each wsシート In ブック.Worksheets
            wsシート.Name = "B-" & wsシート.Name
        Next
    Next
End Sub

'【基礎】
' Do while / Loop で繰り返しの続行条件を記述
' B列に記入がある場合に、C列に済を記入する
Sub ②記入済みチェック()
    Dim i As Long
    i = 1
    Do While Cells(i, 2).Value <> ""
        Cells(i, 3).Value = "済"
        i = i + 1
    Loop
End Sub

'【演習】
' C列の空欄に未納と入力する
Sub ③未納チェック()
    Dim i As Long
    i = 1
    Do While Cells(i, 2).Value <> ""
        If Cells(i, 3).Value = "" Then
            Cells(i, 3).Value = "未納"
        End If
        i = i + 1
    Loop
End Sub

'【アドバンス】
' Exit Do/ Exit For でループを抜けることが可能
Sub ③ナンバー検索()
    Dim i As Long
    i = 1
    Do While Cells(i, 2).Value <> ""
        If Cells(i, 2).Value = "C" Then
            MsgBox "CさんのNo.は" & Cells(i, 1)
            Exit Do
        End If
        i = i + 1
    Loop
End Sub


