Option Explicit

' 【演習】===================================================================
' 一つのエクセルを開いてデータ数を調べる
' Workbooksコレクション.Open(FileName)　でエクセルを開く
' Wrokbookオブジェクト.Close でエクセルを閉じる

Sub エクセルOpen()
    Dim パス As String
    Dim データ数 As Long
    
    ChDir ThisWorkbook.Path
    
    パス = "7.ExcelFiles\201901\支店0107\札幌_0107.xlsx"
    
    ' エクセルオープン
    Workbooks.Open パス
    
    ' データ数の取得
    データ数 = Range("A1").End(xlDown).Row - 1
    MsgBox パス & ":" & データ数
    
    ' エクセルのクローズ
    ActiveWorkbook.Close
End Sub


' 【基礎】==================================================================
' フォルダ内のエクセルのパスを調べる
' Dir() で一致するファイルを検索する（無ければ""が返ってくる)
Sub ファイルパス確認()
    Dim ファイル名 As String
    
    ' Dirで一致するファイルを検索
    ファイル名 = Dir("7.ExcelFiles\201901\支店0107\*.xlsx")
    MsgBox ファイル名
    
    ' 次のファイルを見たい場合は引数無しでDirとする
    ファイル名 = Dir
    MsgBox ファイル名
End Sub

' 【演習】==================================================================
' フォルダ内のエクセルをすべて開く
Sub 複数エクセルオープン()
    Dim パス As String
    Dim データ数 As Long
    Dim ファイル名 As String
    
    パス = "7.ExcelFiles\201901\支店0107\"
    ファイル名 = Dir(パス & "*.xlsx")
    
    ' ファイル名が空になるまで繰り返す
    Do While ファイル名 <> ""
       ' エクセルオープン
        Workbooks.Open パス & ファイル名

        ' データ数の取得
        データ数 = Range("A1").End(xlDown).Row - 1
        MsgBox ファイル名 & ":" & データ数
    
        ' エクセルのクローズ
        ActiveWorkbook.Close
        
        ' ファイル名の更新
        ファイル名 = Dir
    Loop
End Sub


' 【①演習】=======================================================================
' 指定したフォルダ内のエクセルを統合する

Sub 複数エクセル統合()
    Dim パス As String
    Dim データ数 As Long
    Dim ファイル名 As String
    Dim 貼付行 As Long
    Dim ws統合 As Worksheet
    
    パス = Range("C4").Value
    ファイル名 = Dir(パス & "*.xlsx")
    
    ' シート名を取得し、ws統合にシートを格納
    Set ws統合 = Worksheets(Range("C5").Value)
        
    
    ' ファイル名が空になるまで繰り返す
    Do While ファイル名 <> ""
        MsgBox "ファイル名:" & ファイル名
      
        ' エクセルオープン
        Workbooks.Open パス & ファイル名

        ' データ数の取得
        データ数 = Range("A1").End(xlDown).Row - 1
        MsgBox "データ数:" & データ数
        
        ' xldownで同じようにやりたいところだが、A1をアクティブにしてctrl+↓を押す動作なので
        ' 1行しかないときにうまくいかない
        ' Rows.Count で一番下の行に行った後、ctrl+↑を押すことで、対応可能
        貼付行 = ws統合.Cells(Rows.Count, 1).End(xlUp).Row + 1
        MsgBox 貼付行 & "行から貼り付けます..."
        
        ' A2を中心にリサイズして、コピーを行う
        ' Destination はコピー先の左上セルを指定
        Range("A2").Resize(データ数, 6).Copy _
            Destination:=ws統合.Cells(貼付行, 1)
        
        ' エクセルのクローズ
        ActiveWorkbook.Close
        
        ' ファイル名の更新
        ファイル名 = Dir
    Loop
    ws統合.Select
End Sub
