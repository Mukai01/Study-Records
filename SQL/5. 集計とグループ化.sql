-- 1. 集計関数-----------------------------------------------------
-- 集計関数の場合は、関数を使った結果、行の数が変わる
-- Nullは無視して集計される
SELECT SUM(出金額) AS 出金額の合計,
       AVG(出金額) AS 平均出金額,
       MAX(出金額) AS 最も大きな散財,
       MIN(出金額) AS 最も少額の支払い
  FROM 家計簿

-- Nullを0として集計するには
SELECT AVG(COALESCE(出金額, 0)) AS 出金額の平均
  FROM 家計簿

-- Count(*) : 行数を数える
-- Count(入金額) : Nullを除いた行数を数える
SELECT COUNT(*) AS 食費の行数
  FROM 家計簿
 WHERE 費目 = '食費'

-- 重複なしでカウント
SELECT COUNT(DISTINCT 費目) FROM 家計簿

-- 2. グループ別の集計----------------------------------------------
-- Where処理 ⇒ Groupbyに従って分類 ⇒ 集計関数の処理 が行われる
-- SELECTには、GROUPBYの対象 と 集計の対象が入る
SELECT 費目, SUM(出金額) AS 費目別の出金額合計
  FROM 家計簿
 WHERE 出金額 > 0
 GROUP BY 費目

-- 集計後の絞り込みを行うには where ではなくて having句を使用する
SELECT 費目, SUM(出金額) AS 費目別の出金額合計
  FROM 家計簿
 GROUP BY 費目
HAVING SUM(出金額) > 0

-- Select文の全貌
SELECT 選択列リスト
  FROM テーブル名
  -- WHERE 条件式
  -- GROUP BY グループ化列名
  -- HAVING 集計関数に対する条件式
  -- ORDER BY 並び替え列名
