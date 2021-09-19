-- 1. 計算式を使う--------------------------------------------
-- 全ての行に100を足したり、SQLと入力
SELECT 出金額, 
　     出金額 + 100 AS 百円増しの出金額, -- AS で列名を指定できる 
       'SQL' AS 言語
  FROM 家計簿 

-- INSERT文に使用
-- 出金額が1105 の行を追加する
INSERT INTO 家計簿 
            (出金額)
     VALUES (1000 + 105)

-- UPDATE文に使用
-- 出金額を +100にする
UPDATE 家計簿
   SET 出金額 = 出金額 + 100


-- 2. 様々な演算子---------------------------------------------
-- 値を変換するCASE 演算子
-- 費目が　居住費の時に 固定費 という列を作る
SELECT 費目, 出金額,
  CASE 費目 WHEN '居住費' THEN '固定費'
            WHEN '水道光熱費' THEN '固定費'
            ELSE '変動費'
   END AS 出費の分類
  FROM 家計簿 WHERE 出金額 > 0

-- WHEN の後ろに条件式を記入する文法
SELECT 費目, 入金額,
  CASE WHEN 入金額 < 5000 THEN 'お小遣い'
       WHEN 入金額 < 100000 THEN '一時収入'
       WHEN 入金額 < 300000 THEN '給料'
       ELSE '想定外の収入です'
   END AS 収入の分類
  FROM 家計簿 WHERE 入金額 > 0


-- 3. 文字に関する関数---------------------------------------------
-- 文字の長さを取得: Length
SELECT メモ, LENGTH(メモ) AS メモの長さ FROM 家計簿
 WHERE LENGTH(メモ) <= 10

-- 空白を除去する: TRIM/LTRIM/RTRIM
SELECT メモ, TRIM(メモ) AS 空白除去したメモ
  FROM 家計簿

-- メモの一部を置換する: Replace
-- メモ列の「購入」を「買った」に置換
UPDATE 家計簿
   SET メモ = REPLACE(メモ, '購入', '買った')

-- 一部を抽出する: Substring
-- 1文字目から3文字抽出し、「費」という文字があれば抽出
SELECT * FROM 家計簿
 WHERE SUBSTRING(費目, 1, 3) LIKE '%費%'

-- 文字列の連結
-- || で連結
SELECT 費目||':'||メモ FROM 家計簿

-- CONCATで連結
SELECT CONCAT(費目, ':', メモ) FROM 家計簿


-- 4. 数値にまつわる関数---------------------------------------
-- 指定桁で四捨五入: Round
-- -2 だと整数部の2桁目で四捨五入、正だと小数の桁数になる
SELECT 出金額, ROUND(出金額, -2) AS 百円単位の出金額
  FROM 家計簿

-- 指定桁で切り捨て: Trunc
SELECT 出金額, TRUNC(出金額, -3) AS 切り捨てた出金額
  FROM 家計簿

-- べき乗を計算: Power
SELECT 出金額, POWER(出金額, 2) AS 出金額の二乗
  FROM 家計簿


-- 5. 日付にまつわる関数
-- CURRENT_TIME: 現在の時間
-- CURRENT_DATE: 現在の日付
INSERT INTO 家計簿
VALUES (CURRENT_DATE, '食費', 'ドーナツを買った', 0, 260)

-- 6. 変換にまつわる関数
-- 型の変換: Cast
-- 出金額を文字型に変換して、円をつける
SELECT (CAST(出金額 AS VARCHAR(20))||'円') FROM 家計簿

-- 最初に登場するNULLでない値を返す: Coalesce
-- 以下のようにするとBが返ってくる
SELECT COALESCE(NULL, 'B','C')

-- これを利用して、欠損値の補完が可能
-- 欠損値を作成
INSERT INTO 家計簿
VALUES (CURRENT_DATE,'食費', NULL, 0, 280);

-- 欠損値を補完
SELECT 日付, 費目,
       COALESCE (メモ, '(メモはNULLです)') AS メモ,
       入金額, 出金額
  FROM 家計簿

-- 7. 関数の確認
-- SELECTを使用して、関数の動きを確認することが可能
SELECT ROUND(280,-2)