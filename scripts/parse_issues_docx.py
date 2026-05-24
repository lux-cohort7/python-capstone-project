"""Parse 120_GitHub_Issues.docx into structured issue dicts."""
import json
import re
import sys
import zipfile
import xml.etree.ElementTree as ET
from pathlib import Path

PROJECT_BRANCHES = [
    ("student_results", "project/student-results", 1, 24),
    ("expense_tracker", "project/expense-tracker", 25, 48),
    ("shop_inventory", "project/shop-inventory", 49, 72),
    ("matatu_fare", "project/matatu-fare", 73, 96),
    ("hospital_records", "project/hospital-records", 97, 120),
]


def docx_text(path: Path) -> str:
    with zipfile.ZipFile(path) as z:
        root = ET.fromstring(z.read("word/document.xml"))
    texts = []
    for t in root.iter(
        "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}t"
    ):
        if t.text:
            texts.append(t.text)
        if t.tail:
            texts.append(t.tail)
    return "".join(texts)


def project_branch_for(num: int) -> str:
    for _, branch, start, end in PROJECT_BRANCHES:
        if start <= num <= end:
            return branch
    raise ValueError(f"No project branch for issue #{num}")


def parse_issues(full: str) -> list[dict]:
    chunks = re.split(r"(?=#\d+Write )", full)
    issues = []
    for chunk in chunks:
        m = re.match(
            r"#(\d+)Write (.+?)Task(.+?)Test(.+?)Output(.+?)Branchissue-(\d+)/([^\s\[]+)\s*\[([^\]]+)\]",
            chunk,
            re.DOTALL,
        )
        if not m:
            continue
        num = int(m.group(1))
        title = f"Write {m.group(2).strip()}"
        task = m.group(3).strip()
        test = m.group(4).strip()
        output = m.group(5).strip()
        student_branch = f"issue-{m.group(6)}/{m.group(7)}"
        label = m.group(8).strip()
        issues.append(
            {
                "number": num,
                "title": title,
                "task": task,
                "test": test,
                "output": output,
                "student_branch": student_branch,
                "project_branch": project_branch_for(num),
                "label": label,
            }
        )
    issues.sort(key=lambda x: x["number"])
    return issues


def format_body(issue: dict) -> str:
    return (
        f"## Task description\n\n{issue['task']}\n\n"
        f"## Test to run\n\n```python\n{issue['test']}\n```\n\n"
        f"## Expected output\n\n```\n{issue['output']}\n```\n\n"
        f"## Branch\n\nWork on branch: `{issue['student_branch']}`\n\n"
        f"Project branch: `{issue['project_branch']}`"
    )


def main() -> None:
    docx = Path(__file__).resolve().parents[1] / "120_GitHub_Issues.docx"
    full = docx_text(docx)
    issues = parse_issues(full)
    if len(issues) != 120:
        print(f"WARNING: parsed {len(issues)} issues, expected 120", file=sys.stderr)
    out = Path(__file__).resolve().parent / "issues.json"
    out.write_text(json.dumps(issues, indent=2), encoding="utf-8")
    print(f"Wrote {len(issues)} issues to {out}")


if __name__ == "__main__":
    main()
