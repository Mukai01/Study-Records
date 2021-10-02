-- 1. データベースを使う2つの立場------------------------------------------------------
-- データの出し入れを行う
-- DML (Data Manipulation Language) : SELECT, INSERT, UPDATE, DELETE
-- TCL (Transaction Conrtol Language) : COMMIT, ROLLBACK, SET TRANSACTION

-- テーブルを作成する
-- DDL (Data Definition Language) : CREATE, ALTER, DROP, TRUNCATE
-- DCL (Data Conrtol Language) : GRANT, REVOKE

-- DCLはデータ操作の権限を設定するもので、管理者が実行する
GRANT 権限名 TO ユーザー名 -- 権限を付与
REVOKE 権限名 FROM ユーザー名 -- 権限をはく奪


-- 2. テーブルの作成----------------------------------------------------------------
CREATE TABLE 家計簿 (
    日付    DATE,
    費目ID　INTEGER,
    MEMO    VARCHAR(100),
    入金額  INTEGER,
    出金額  INTEGER
)

-- デフォルト値の設定
CREATE TABLE 家計簿 (
    日付    DATE,
    費目ID  INTEGER,
    MEMO    VARCHAR(100) DEFAULT '不明',
    入金額  INTEGER      DEFAULT 0,
    出金額  INTEGER      DEFAULT 0
)

-- テーブルの削除
DROP TABLE 家計簿

-- 列の追加
ALTER TABLE 家計簿 ADD 関連日 DATE;

-- 列の削除
ALTER TABLE 家計簿 DROP 関連日

-- 全件のデータを削除
-- テーブルを消して、同じものを作るので処理が速い
TRUNCATE TABLE 家計簿


-- 3. 制約----------------------------------------------------------------
-- NOT NULL: NULLが入らない
-- CHECK: 格納される値が妥当か確認
CREATE TABLE 家計簿 (
    日付    DATE         NOT NULL,
    費目ID  INTEGER,
    MEMO    VARCHAR(100) DEFAULT '不明' NOT NULL,
    入金額  INTEGER      DEFAULT 0 CHECK (入金額 >= 0),
    出金額  INTEGER      DEFAULT 0 CHECK (出金額 >= 0)
);

-- UNIQUE: 重複があってはならない
CREATE TABLE 費目(
    ID      INTEGER,
    名前    VARCHAR(40)  UNIQUE
);

-- 主キーにはPRIMARY KEY制約を与える
-- NULLも重複も許さない
CREATE TABLE 費目(
    ID      INTEGER     PRIMARY KEY,
    名前    VARCHAR(40) UNIQUE
);

-- 4. 参照整合性------------------------------------------------------------------
-- リレーションシップがきちんと成立していることを参照整合性という
-- 参照整合性制約を崩す操作にエラーを返すのが外部キー制約
-- 外部キー制約の対象はPRIMARY KEY もしくは UNIQUE 制約が必要
CREATE TABLE 家計簿 (
    日付    DATE         NOT NULL,
    費目ID  INTEGER      REFERENCES 費目(ID), -- 外部キー制約
    MEMO    VARCHAR(100) DEFAULT '不明' NOT NULL,
    入金額  INTEGER      DEFAULT 0 CHECK (入金額 >= 0),
    出金額  INTEGER      DEFAULT 0 CHECK (出金額 >= 0)
);
