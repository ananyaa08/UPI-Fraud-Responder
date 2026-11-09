"""Runs every test case and writes UNEDITED outputs to outputs/. Re-run after setting your API key."""
import os
from dotenv import load_dotenv

load_dotenv()
from core import Case, respond, llm_status  # noqa: E402
from tests.cases import CASES  # noqa: E402

os.makedirs("outputs", exist_ok=True)
summary = [f"# Test run summary\n\nMode: {llm_status()}\n"]
for cid, desc, turns in CASES:
    case = Case()
    log = [f"# {cid}\n{desc}\n"]
    last_report = None
    for t in turns:
        res = respond(case, t)
        log.append(f"## USER\n{t}\n\n## BOT\n{res['text']}\n")
        if res["report"]:
            last_report = res["report"]
    if last_report:
        log.append("## FINAL REPORT\n```\n" + last_report + "\n```\n")
    log.append(f"## STATE\ncategory={case.category} score={case.category_score:.3f} in_scope={case.in_scope} "
               f"amount={case.amount} utr={case.utr} upi={case.upi_id} phone={case.suspect_phone} "
               f"bank={case.bank} platform={case.platform} time={case.txn_time}\n")
    open(f"outputs/{cid}.md", "w", encoding="utf-8").write("\n".join(log))
    summary.append(f"- {cid}: in_scope={case.in_scope} category={case.category} ({case.category_score:.2f}) "
                   f"amount={case.amount} utr={case.utr} suspect={case.upi_id or case.suspect_phone} "
                   f"bank={case.bank} report={'yes' if last_report else 'no'}")
open("outputs/_summary.md", "w", encoding="utf-8").write("\n".join(summary))
print("\n".join(summary))
