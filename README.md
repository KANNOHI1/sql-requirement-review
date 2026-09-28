# sql-requirement-review

BigQuery の SQL が業務要件（営業の質問）と合っているかをレビューする、Gemini CLI / Claude Code 用の Skill。
AI エージェントやエンジニアが書いた SQL を、要件の分解 → SQL の逆翻訳 → 突き合わせ → 罠チェック（15 項目）→ 読み取り専用の実行確認 の順で点検し、判定（合致／要確認／不一致）・ズレ一覧・エンジニアへの確認質問を返す。

**このリポジトリに実データ・社名・実テーブル名は含まない。** テストは架空の化粧品卸「ミツキ化粧品」のデータ（`tests/datasets.sql`、[sql-reading-dojo](https://github.com/KANNOHI1/sql-reading-dojo) から複製）で行う。

## 構成

```
skill/                          ← 配布するのはここだけ
  SKILL.md                      手順と出力形式
  references/trap-checklist.md  罠 15 項目（見つけ方・Alteryx 対応・典型的な被害）
  references/metric-definitions.md  指標定義表の雛形（使う環境で記入する）
tests/
  cases.yaml                    罠入り SQL 12 本 + 正しい SQL 2 本
  datasets.sql                  架空データ
  check_cases.py                ケース自体の正しさを DuckDB で検証
  schema.md / metric-definitions.md  テスト用のテーブル定義・指標定義
```

## 配置（Gemini CLI）

```bash
git clone https://github.com/KANNOHI1/sql-requirement-review.git
mkdir -p ~/.gemini/skills/sql-requirement-review
cp -r sql-requirement-review/skill/. ~/.gemini/skills/sql-requirement-review/
```

Gemini CLI を再起動し、`/skills` に `sql-requirement-review` が出ることを確認する。Claude Code なら `~/.claude/skills/` に同じ形で置く。

## 使い方

要件と SQL を 1 ファイル（例: `req01.md`）に置き、

```
@req01.md を sql-requirement-review スキルでレビューして。結果は req01_result.md に保存して
```

`bq` が使える環境では dry run と件数確認まで行う。実行は SELECT と `--dry_run` に限る（SKILL.md 手順 5）。

## テスト

```bash
pip install duckdb pyyaml
python tests/check_cases.py
```

罠入りケースは正解 SQL と結果が違うこと、正しいケースは一致することを確かめる（ケース自体の嘘を防ぐ）。Skill の検出精度は、答えを伏せた別モデルに SKILL.md どおりレビューさせて測った（v1: 14/14 × 2 周。T13〜T15 は未テスト）。
