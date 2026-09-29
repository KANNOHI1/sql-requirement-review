---
description: git から文脈を復帰する（STATUS は全文を読まない）
---
次を順に実行し、最後に 1 行で復帰を報告する。

1. `git pull --rebase origin <現在のブランチ>`
2. `CLAUDE.md` の「目標」を確認する
3. `docs/STATUS.md` は**全文を読まない**。次の 2 つだけ
   - `sed -n '/^## 現在地/,/^## 次にやること/p' docs/STATUS.md`
   - `grep -n '^\- \[U-' docs/STATUS.md | grep -v 'クローズ'`
4. `git log --oneline -20`
5. `tail -n 5 docs/journal.md` に「着手」のまま残っている行があれば、二重作業しないよう、その作業の実体ファイルを確認してから進める

報告は 1 行: 「復帰: 現在地＝…、未解決 N 件、直近 commit …」
