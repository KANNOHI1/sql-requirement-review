-- このリポジトリ独自の追加データ（sql-reading-dojo の datasets.sql には含まれない）。
-- check_cases.py が datasets.sql の後に読み込む。T14（元データの重複行）の題材。

-- 基幹システムからの取込生データ。sales と同じ列構成だが、再送により同じ sale_id が複数行入ることがある。
-- T014 と T019 が 2 回入っている（内容は同一）。
CREATE TABLE dojo.sales_raw (
  sale_id    STRING    NOT NULL,
  sale_ts    TIMESTAMP NOT NULL,
  store_id   STRING    NOT NULL,
  product_id STRING    NOT NULL,
  qty        INT64     NOT NULL,
  amount     INT64,
  loaded_at  TIMESTAMP NOT NULL   -- 取り込んだ日時
);
INSERT INTO dojo.sales_raw
SELECT sale_id, sale_ts, store_id, product_id, qty, amount, sale_ts + INTERVAL 1 HOUR
FROM dojo.sales;
INSERT INTO dojo.sales_raw VALUES
  ('T014', TIMESTAMP '2026-06-01 01:00:00', 'S03', 'P001', 12, 45600, TIMESTAMP '2026-06-01 03:00:00'),
  ('T019', TIMESTAMP '2026-06-15 04:55:00', 'S12', 'P001', 6,  22800, TIMESTAMP '2026-06-15 07:00:00');
