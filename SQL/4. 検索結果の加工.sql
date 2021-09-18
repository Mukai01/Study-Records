-- 1. 重複行を削除する---------------------------------------
SELECT DISTINCT 費目 FROM 家計簿

-- 2. 並べ替える--------------------------------------------
SELECT * FROM 家計簿
 ORDER BY 日付 DESC -- DESCが無いと昇順になる

-- 複数列で並び替え
SELECT * FROM 家計簿
 ORDER BY 入金額 DESC, 出金額 ASC

-- 列番号で並び替えることも可能
SELECT 入金額, 出金額 FROM 家計簿 ORDER BY 1 DESC, 2 ASC

-- 3. 先頭から数行だけ取得する---------------------------------
-- 0行目から次の3行を取得
SELECT 費目, 出金額 FROM 家計簿
 ORDER BY 出金額 DESC
OFFSET 0 ROWS
 FETCH NEXT 3 ROWS ONLY

-- 4. 集合演算子--------------------------------------------
-- 列数とデータ型が一致しているときに UNION でつなげることができる
-- order by は最後のSELECT文に記述する
-- 列番号以外による指定の場合、1つめのSELECT文のものを指定する
SELECT 費目, 入金額, 出金額 FROM 家計簿
 UNION
SELECT 費目, 入金額, 出金額 FROM 家計簿アーカイブ
 ORDER BY 2,3,1

-- 差集合を取得するときは EXCEPT
-- 家計簿だけにある費目を抽出
SELECT 費目 FROM 家計簿
EXCEPT
SELECT 費目 FROM 家計簿アーカイブ

-- 積集合を取得するときは INTERSECT
SELECT 費目 FROM 家計簿
INTERSECT
SELECT 費目 FROM 家計簿アーカイブ