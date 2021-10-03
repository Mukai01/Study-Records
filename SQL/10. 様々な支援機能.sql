-- 1. データベースを早くする--------------------------------------
-- インデックスを作成すると、検索が早くなる
-- インデックス名をつける
CREATE INDEX 費目IDインデックス ON 家計簿(費目ID);
CREATE INDEX メモインデックス ON 家計簿(メモ);

-- インデックスの削除
DROP INDEX 費目IDインデックス

-- インデックスを作っておいて、WHERE句で絞り込む時早くなる
SELECT * FROM 家計簿
 WHERE メモ = '不明'

-- 前方一致検索でも早くなる
-- 後方一致、部分一致ではインデックスを使用できない
SELECT * FROM 家計簿
 WHERE メモ LIKE '1月の%'

-- Order by による並び替えも早くなる
SELECT * FROM 家計簿
 ORDER BY 費目ID

-- JOINによる結合も早くなる
SELECT * FROM 家計簿
  JOIN 費目
    ON 家計簿.費目ID = 費目.費目ID

-- インデックスを作りすぎると、テーブルデータを書き換えたときに、インデックスも書き換えなければならない

-- 2. データベースをより便利にする

-- ビューを作成し、テーブルのように扱う
-- 家計簿4月のビューを作成する
CREATE VIEW 家計簿4月 AS
SELECT * FROM 家計簿
 WHERE 日付 >= '2018-04-01'
   AND 日付 <= '2018-04-30' 

-- これにより、SQL文がシンプルになる
SELECT * FROM 家計簿4月;
SELECT DISTINCT 費目 FROM 家計簿4月;

-- ビューはあくまで、名前を付けたSELECT文
-- INSERTやUPDATEは使えない

-- 採番の方法
-- SQLiteの場合以下のように設定すると、自動でIDに連番が割り振られる
CREATE TABLE 費目(
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    ...,
)

-- PostgreSQL 等には連番を管理してくれる専用の道具としてシーケンスがある
-- シーケンスの作成
CREATE SEQUENCE 費目シーケンス;
-- 現在の値を取得
SELECT CURRVAL('費目シーケンス');
-- 次の値に進み、その値を取得
SELECT NEXTVAL('費目シーケンス');

-- 副問い合わせにシーケンスを使用することで自動採番
INSERT INTO 費目(ID, 名前)
     VALUES (
         ( SELECT NEXTVAL('費目シーケンス')), '接待交際費'
     )

-- 最大値から連番を取得する方法も考えられるが、お勧めできない
-- 複数の人に同じ番号が採番されてしまう
-- 最後の行を削除後、同じ番号が使用されてしまう
SELECT MAX(ID) + 1 AS 採番 FROM 費目