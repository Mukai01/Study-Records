-- 1. 様々な条件式--------------------------------------------------------------
-- 欠損値の判定は IS NULL
SELECT *
  FROM 家計簿
 WHERE 出金額 IS NULL -- 否定の場合は IS NOT NULL

-- パターンマッチング
-- % : 任意の0文字以上の文字列
-- _ : 任意の1文字
SELECT * FROM 家計簿
 WHERE メモ LIKE '%1月%'

-- %や_にマッチングさせたい場合は、ESCAPE文字を指定して、前につける
SELECT * FROM 家計簿 
 WHERE メモ LIKE '%100$%' ESCAPE '$'

-- 範囲判定
SELECT * FROM 家計簿
 WHERE 出金額 BETWEEN 100 AND 3000

-- IN/NOT IN 演算子
SELECT * FROM 家計簿
 WHERE 費目 IN ('食費', '交際費') --否定の場合は NOT IN

-- ANY/ALL 演算子（単体で使うメリットは無い）
SELECT * FROM 家計簿
 WHERE 出金額 < ANY (1000, 2000, 3000) -- いずれかよりも小さければTrueになる

SELECT * FROM 家計簿
 WHERE 出金額 < ALL (1000, 2000, 3000) -- いずれよりも小さければTrueになる

-- AND/OR/NOT 演算子
-- ()をつけることで優先順位が上がる
 SELECT * FROM 家計簿
 WHERE (日付 = '20180203'
	OR NOT 日付 = '20180211')
   AND 出金額 > 500

-- 主キー: 1行を完全に特定できる役割を持つ列