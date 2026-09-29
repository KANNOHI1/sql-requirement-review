"""ブラインド評価用の入力ファイルを作る。

    python tests/make_blind_inputs.py C13 C14 C15 [--out DIR]

cases.yaml から要件と SQL だけを取り出し、schema.md と metric-definitions.md を添える。
trap / expected / reference は含めない。既定の出力先は tests/blind-eval/inputs/（.gitignore 済み）。
"""
import argparse
from pathlib import Path

import yaml

HERE = Path(__file__).parent


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("ids", nargs="+")
    ap.add_argument("--out", default=str(HERE / "blind-eval" / "inputs"))
    args = ap.parse_args()

    out = Path(args.out)
    out.mkdir(parents=True, exist_ok=True)
    schema = (HERE / "schema.md").read_text(encoding="utf-8")
    metrics = (HERE / "metric-definitions.md").read_text(encoding="utf-8")
    cases = {c["id"]: c for c in yaml.safe_load((HERE / "cases.yaml").read_text(encoding="utf-8"))}

    for cid in args.ids:
        c = cases[cid]
        text = (f"# レビュー依頼 {cid}\n\n## 要件\n{c['requirement']}\n\n"
                f"## SQL\n```sql\n{c['sql']}```\n\n## テーブル定義\n{schema}\n\n## 指標定義\n{metrics}\n")
        (out / f"{cid}.md").write_text(text, encoding="utf-8")
        print(out / f"{cid}.md")


if __name__ == "__main__":
    main()
