# 作業ログ

形式: `日時（JST）｜要旨｜状態`。着手前に「着手」で 1 行書いて push し、終わったら「完了（commit ハッシュ）」へ書き換える。新しい行は末尾に足す。

2026-09-29 13:40｜v1 初回コミット（Skill 本体・罠 15 項目・テスト 14 ケース）｜完了（ae09a07）
2026-09-29 14:21｜C13〜C15 追加、datasets_extra.sql 新設、SKILL.md の項目数修正、ブラインド評価 3/3｜完了（aa50126）
2026-09-29 14:21｜Draft PR #1 作成、監視開始｜完了
2026-09-29 14:32｜文脈を git に逃がす運用（CLAUDE.md / STATUS / journal / save / recall / フック）を追加｜完了（83867e7）
2026-09-29 14:35｜PR #1 を main にマージ（merge commit bbab8b4。squash にすると journal に書いた 83867e7 が main から辿れなくなるため merge を選択）、監視と定期確認を解除、作業ブランチを main から再開｜完了
2026-09-29 14:37｜前回 /save の漏れを補完: ブラインド評価の手順（tests/blind-eval/README.md）、入力生成スクリプト、C13〜C15 の出力全文、マージ方式の理由｜完了（47b8624）
2026-09-29 14:40｜/save の手順 1 に「根拠と手順も実物で保存する」を追記、手順 4 の git 順序を add → commit → pull → push に修正｜完了（4a62eb7）
2026-09-29 14:58｜K03〜K10（罠に見える正しい SQL）を追加してブラインド評価で過剰検出を測る。誤検出した項目の判断基準を SKILL/checklist に追記、会社 Gemini CLI 用の試行手順（docs/field-trial.md）を新設｜完了（b694f62・a92737c・field-trial は次の commit）
2026-09-29 15:27｜持ち帰り票の規則を skill/references/carry-sheet.md に移し、SKILL.md に参照を追加、field-trial.md 第 1 節を 1 行の指示文に差し替え｜着手
