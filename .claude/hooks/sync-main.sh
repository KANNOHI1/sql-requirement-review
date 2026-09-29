#!/usr/bin/env bash
# SessionStart（startup / resume / clear）で実行。現在のブランチを pull し、直近の状況を標準出力に出す。
# 標準出力はそのまま会話の文脈に入る。失敗しても exit 0 で終える。
cd "${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel 2>/dev/null || pwd)}" || exit 0

branch=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)
before=$(git rev-parse HEAD 2>/dev/null)
echo "[sync] branch: ${branch}"
if git rev-parse --abbrev-ref '@{upstream}' >/dev/null 2>&1; then
  if out=$(git pull --rebase --autostash 2>&1); then
    after=$(git rev-parse HEAD 2>/dev/null)
    n=$(git rev-list --count "${before}..${after}" 2>/dev/null || echo 0)
    echo "[sync] pulled ${n} commit(s)"
  else
    echo "[sync] pull failed (続行): $(echo "$out" | tail -n 1)"
  fi
else
  echo "[sync] upstream 未設定のため pull しない"
fi

echo "[sync] recent commits:"
git log --oneline -5 2>/dev/null | sed 's/^/  /'

if [ -f docs/journal.md ]; then
  echo "[sync] docs/journal.md tail:"
  tail -n 5 docs/journal.md | sed 's/^/  /'
fi

if [ -f docs/memory.md ]; then
  echo "[memory] docs/memory.md:"
  cat docs/memory.md
fi
exit 0
