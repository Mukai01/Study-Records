-- 重複行を削除する
SELECT DISTINCT 費目 FROM 家計簿

-- 並べ替える
SELECT * FROM 家計簿
 ORDER BY 日付 DESC -- DESCが無いと昇順になる

-- 複数列で並び替え
SELECT * FROM 家計簿
 ORDER BY 入金額 DESC, 出金額 ASC

-- 列番号で並び替えることも可能
SELECT 入金額, 出金額 FROM 家計簿 ORDER BY 1 DESC, 2 ASC