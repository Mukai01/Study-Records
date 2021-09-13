-- SELECT, UPDATE, DELETE, INSERT の4命令をDML(Data Manipulation Language)と呼ぶ

-- まずはSelect文の書き方
-- データを選択する
SELECT 費目, 入金額, 出金額
  FROM 家計簿

-- 全て選択する場合
SELECT *
  FROM 家計簿

-- ASによる別名を定義 
SELECT 費目 AS ITEM, 入金額 AS RECEIVE, 出金額 AS PAY
  FROM 家計簿 AS MONEYBOOK
 WHERE 費目 = '給料' -- 費目が給料のみを抽出


-- UPDATE文の書き方
-- データを更新する
 UPDATE 家計簿
   SET 入金額 = 9999
 WHERE 日付 = '2018-02-03'


-- DELETE文の書き方
-- 行を削除する
 DELETE
  FROM 家計簿
 WHERE 日付 = '2018-02-03'

 -- INSERT文の書き方
 -- 行を挿入する
 INSERT INTO 家計簿
             (費目, 日付, 出金額)
	    VALUES ('通信費', '2018-02-20', 6200)

 -- 2行目はすべての場合は省略可能
 INSERT INTO 家計簿
	    VALUES ('2018-02-20', '通信費', '携帯電話料金', 0, 6200)