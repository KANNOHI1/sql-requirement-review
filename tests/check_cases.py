"""テストケース自体の正しさを DuckDB で検証する。

罠ありケース（expected=不一致）は sql と reference の結果が違うこと、
正解ケース（expected=合致）は結果が一致することを確かめる。
データは sql-reading-dojo の content/datasets.sql を複製した tests/datasets.sql。

    python tests/check_cases.py
"""
import re
import sys
from pathlib import Path

import duckdb
import yaml

HERE = Path(__file__).parent
DATASETS = HERE / "datasets.sql"  # sql-reading-dojo の content/datasets.sql の複製


def to_duckdb(sql: str) -> str:
    """BigQuery 表記のうち、ケースで使う分だけ DuckDB 表記に直す。"""
    sql = sql.replace("`", "")
    sql = re.sub(r"DATE\(([\w.]+),\s*'([^']+)'\)",
                 r"CAST(timezone('\2', CAST(\1 AS TIMESTAMPTZ)) AS DATE)", sql)
    return re.sub(r"DATE\(([\w.]+)\)", r"CAST(\1 AS DATE)", sql)


def rows(con, sql: str, ordered: bool) -> list:
    result = [tuple(round(v, 6) if isinstance(v, float) else v for v in r)
              for r in con.execute(to_duckdb(sql)).fetchall()]
    return result if ordered else sorted(result, key=repr)


def main() -> int:
    con = duckdb.connect()
    con.execute("SET TimeZone='UTC'")
    con.execute(DATASETS.read_text(encoding="utf-8"))

    failed = 0
    for case in yaml.safe_load((HERE / "cases.yaml").read_text(encoding="utf-8")):
        ordered = "ORDER BY" in case["reference"]
        got = rows(con, case["sql"], ordered)
        ref = rows(con, case["reference"], ordered)
        ok = (got != ref) if case["expected"] == "不一致" else (got == ref)
        failed += not ok
        print(f"{'OK ' if ok else 'NG '} {case['id']} {case['trap']:<4} "
              f"sql={got[:4]}{'…' if len(got) > 4 else ''} ref={ref[:4]}{'…' if len(ref) > 4 else ''}")
    print(f"\n{'全ケース OK' if not failed else f'NG {failed} 件'}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
