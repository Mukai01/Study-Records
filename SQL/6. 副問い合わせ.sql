-- 1. 検索結果に基づいて表を操作する---------------------------------------
-- 内側に別のセレクト文を内包しているネスト構造になっている
-- 他のSQL文の一部分として登場するSELECT文を副問い合わせという
-- 丸カッコでくくって記述する

SELECT 費目, 出金額 FROM 家計簿
 WHERE 出金額 = (SELECT MAX(出金額) FROM 家計簿)


-- 2. 単一行副問い合わせ--------------------------------------------------
-- 家計簿アーカイブの 食費の平均を 家計簿集計の 平均の食費に入力する
UPDATE 家計簿集計
   SET 平均 = (SELECT AVG(出金額)
                FROM 家計簿アーカイブ
               WHERE 出金額 > 0
                 AND 費目 = '食費')
 WHERE 費目 = '食費'

-- 家計簿集計の食費の合計を過去の合計額列として、他のデータにくっつける
SELECT 日付, メモ, 出金額,
       (SELECT 合計 FROM 家計簿集計
       　WHERE 費目 = '食費') AS 過去の合計額
　FROM 家計簿アーカイブ
 WHERE 費目 = '食費'

-- 3. 複数行副問い合わせ--------------------------------------------------
-- IN を使った条件式
-- 家計簿の重複を除いた費目リストに一致するデータのみ抽出
SELECT * FROM 家計簿集計
 WHERE 費目 IN (SELECT DISTINCT 費目 FROM 家計簿)

-- ANY/ALL演算子
-- 家計簿アーカイブの出金額のいずれかより小さければ
SELECT * FROM 家計簿
 WHERE 費目 = '食費'
   AND 出金額 < ANY (SELECT 出金額 FROM 家計簿アーカイブ
                      WHERE 費目 = '食費') -- ALLにすると、いずれよりも小さければとなる

-- 副問い合わせの中にNULLがあると、 NOT INを使うと常にNULLになってしまう
SELECT * FROM 家計簿
 WHERE 費目 NOT IN ('食費', '水道光熱費', NULL)

-- そこで以下の2手法でNullを除外する
SELECT * FROM 家計簿アーカイブ
 WHERE 費目 IN (SELECT 費目 FROM 家計簿
                 WHERE 費目 IS NOT NULL)

SELECT * FROM 家計簿アーカイブ
 WHERE 費目 IN (SELECT COALESCE(費目, '不明') FROM 家計簿)


-- 4. 表の結果となる副問い合わせ
-- 家計簿と家計簿アーカイブの一部をつなげて、SUMで合計額を計算
-- テーブルにはSUBという名前を付けている
SELECT SUM(SUB.出金額) AS 出金額合計
  FROM (SELECT 日付, 費目, 出金額
          FROM 家計簿
         UNION
        SELECT 日付, 費目, 出金額
          FROM 家計簿アーカイブ
         WHERE 日付 >= '2018-01-01'
           AND 日付 <= '2018-01-31') AS SUB

-- 家計簿集計の4項目に、テーブルを追加する
INSERT INTO 家計簿集計 (費目, 合計, 平均, 回数)
-- 以下が副問い合わせ
-- この用法はInsert文の特殊用法なので、カッコはいらない
SELECT 費目, SUM(出金額), AVG(出金額), 0
  FROM 家計簿
 WHERE 出金額 > 0
 GROUP BY 費目