Option Explicit
'【基礎】
' 条件の前にNot　をつければ否定となる
Sub if文()
    If Range("B2").Value = "A" Or Range("B2").Value = "B" Then
        MsgBox "無料"
    ElseIf Range("B2").Value = "Z" Then
        MsgBox "その他"
    Else
        MsgBox "有料"
    End If
End Sub


' 文字列の判定には Like が使える
' "VBA" Like "V*" はTrueとなる
' *    :任意の文字列
' ?    :任意の1文字
' #    :任意の数字
' [   ]:[]内の1文字
' [!  ]:[]内の文字以外
' [A-D]:文字の範囲(A-D)


' 【アドバンス】
Sub Select_case文()
    Select Case Range("B2").Value
        Case Is = "A"
            MsgBox "A"
        Case Is = "B"
            MsgBox "B"
        Case Else
            MsgBox "F"
    End Select
End Sub