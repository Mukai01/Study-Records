Option Explicit
'【基礎】
' WorksheetFunctionを使用する
Sub WorksheetFunctionを使用()
    MsgBox WorksheetFunction.Sum(Range("B2:B4"))
End Sub

' 今日の日付を取得する
Sub 日付()
    MsgBox Date
End Sub


' セルの値を調べる
' isnumeric : 数字かどうか確認
Sub セルの確認()
    MsgBox IsNumeric(Range("B2"))
End Sub


' データ型の変更
Sub 整数に変換()
    Range("C4").Value = CInt("40") ' cintで整数に変換
End Sub


' インプットボックス
' 改行はvbcrlfで行う
Sub 入力()
    Dim a As Variant ' variantは全ての型を格納可能
    a = InputBox("日付を入力" & vbCrLf & "してください", "請求日の入力", Date) ' 3つ目がデフォルトの指定
End Sub
