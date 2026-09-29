# テーブル定義（テスト用・架空の化粧品卸「ミツキ化粧品」）

データセット `dojo`。BigQuery。`sales` は取引の正本、`sales_raw` は基幹システムからの取込生データ（重複を除く前）。

| 表 | 列 | 型 | 意味 |
|---|---|---|---|
| customers | customer_id | STRING | 得意先 ID |
| | customer_name | STRING | 得意先名 |
| | channel | STRING | チャネル（ドラッグ / GMS / 百貨店 / EC） |
| | region | STRING | 地域（NULL 可） |
| | is_active | BOOL | 稼働中なら TRUE |
| stores | store_id | STRING | 店舗 ID |
| | customer_id | STRING | 所属する得意先 ID（1 得意先に複数店舗） |
| | store_name | STRING | 店舗名 |
| | prefecture | STRING | 都道府県 |
| | opened_date | DATE | 開店日 |
| products | product_id | STRING | 商品 ID |
| | product_name | STRING | 商品名 |
| | brand | STRING | ブランド |
| | category | STRING | カテゴリ |
| | list_price | INT64 | 定価（税抜・円） |
| | launch_date | DATE | 発売日 |
| sales | sale_id | STRING | 取引 ID |
| | sale_ts | TIMESTAMP | 取引日時 |
| | store_id | STRING | 店舗 ID |
| | product_id | STRING | 商品 ID |
| | qty | INT64 | 数量 |
| | amount | INT64 | 実売金額（税抜・円。NULL 可） |
| sales_raw | sale_id | STRING | 取引 ID（再送により同じ ID が複数行入ることがある） |
| | sale_ts | TIMESTAMP | 取引日時 |
| | store_id | STRING | 店舗 ID |
| | product_id | STRING | 商品 ID |
| | qty | INT64 | 数量 |
| | amount | INT64 | 実売金額（税抜・円。NULL 可） |
| | loaded_at | TIMESTAMP | 基幹システムから取り込んだ日時 |
| promotions | promo_id | STRING | 施策 ID |
| | promo_name | STRING | 施策名 |
| | product_id | STRING | 対象商品 ID |
| | start_date | DATE | 開始日 |
| | end_date | DATE | 終了日（この日を含む） |
| targets | customer_id | STRING | 得意先 ID |
| | fiscal_month | DATE | 対象月（月初日） |
| | target_amount | INT64 | 月次売上目標（税抜・円） |
| stock | store_id | STRING | 店舗 ID |
| | product_id | STRING | 商品 ID |
| | snapshot_date | DATE | 在庫を記録した日（日次） |
| | stock_qty | INT64 | その日の在庫数 |
