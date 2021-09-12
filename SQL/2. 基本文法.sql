-- SELECT, UPDATE, DELETE, INSERT の4命令をDML(Data Manipulation Language)と呼ぶ

-- まずはSelect文の書き方
-- 基本
SELECT 費目, 入金額, 出金額
  FROM 家計簿

-- 全て選択する場合
SELECT *
  FROM 家計簿

-- ASによる別名を定義 
SELECT 費目 AS ITEM, 入金額 AS RECEIVE, 出金額 AS PAY
  FROM 家計簿 AS MONEYBOOK
 WHERE 費目 = '給料' -- 費目が給料のみを抽出