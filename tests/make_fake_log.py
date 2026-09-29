"""tools/ の動作確認用に、架空のエージェントログ（xlsx）を cases.yaml から作る。会社のログと同じ列構成。

    python tests/make_fake_log.py OUT.xlsx
"""
import sys
from pathlib import Path

import pandas as pd
import yaml

HERE = Path(__file__).parent


def main() -> None:
    out = Path(sys.argv[1])
    cases = {c["id"]: c for c in yaml.safe_load((HERE / "cases.yaml").read_text(encoding="utf-8"))}
    # (session, rally, user, dept, query, sql, ts)
    plan = [
        ("S1", 1, "u01", "営業1部", cases["K01"]["requirement"], cases["K01"]["sql"], "2026-06-23 10:00"),
        ("S2", 1, "u02", "営業1部", cases["C02"]["requirement"], cases["C02"]["sql"], "2026-06-24 11:00"),
        ("S2", 2, "u02", "営業1部", "それを全体の達成率にして", cases["C11"]["sql"], "2026-06-24 11:05"),
        ("S2", 3, "u02", "営業1部", "ありがとう", "", "2026-06-24 11:06"),
        ("S3", 1, "u03", "営業2部", cases["C14"]["requirement"],
         "SELECT 1;\n" + cases["C14"]["sql"], "2026-07-02 09:30"),  # 複数 SQL（最後が対象）
        ("S4", 1, "u01", "営業1部", cases["C15"]["requirement"], cases["C15"]["sql"], "2026-08-18 15:00"),
    ]
    rows = [{"列1": ts, "department": d, "user_name": u, "conversation_group_id": s, "rally_number": r,
             "user_query": q, "extracted_sql_queries": sql, "suggestion_text": "（回答文）",
             "raw_agent_response": "（生レスポンス）" + (" Error: retry" if s == "S3" else "")}
            for s, r, u, d, q, sql, ts in plan]
    df = pd.DataFrame(rows)
    with pd.ExcelWriter(out) as w:
        df.to_excel(w, sheet_name="rawdata", index=False)
        u01 = df[df.user_name == "u01"].copy()
        u01["正誤判定"] = ["○", "×"]
        u01.to_excel(w, sheet_name="u01", index=False)
        u02 = df[df.user_name == "u02"].copy()
        u02["正誤判定"] = ["×", "", ""]
        u02.to_excel(w, sheet_name="u02", index=False)
    print(out)


if __name__ == "__main__":
    main()
