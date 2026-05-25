"""Create GitHub issues from issues.json for a number range."""
import json
import subprocess
import sys
from pathlib import Path

GH = r"C:\Program Files\GitHub CLI\gh.exe"
REPO = "Navashub/python-capstone-project"


def format_body(issue: dict) -> str:
    return (
        f"## Task description\n\n{issue['task']}\n\n"
        f"## Test to run\n\n```python\n{issue['test']}\n```\n\n"
        f"## Expected output\n\n```\n{issue['output']}\n```\n\n"
        f"## Branch\n\nWork on branch: `{issue['student_branch']}`\n\n"
        f"Project branch: `{issue['project_branch']}`"
    )


def main() -> None:
    start = int(sys.argv[1])
    end = int(sys.argv[2])
    issues_path = Path(__file__).resolve().parent / "issues.json"
    issues = {i["number"]: i for i in json.loads(issues_path.read_text(encoding="utf-8"))}

    print(f"Creating issues #{start}–#{end} on {REPO}\n")
    for num in range(start, end + 1):
        issue = issues[num]
        body = format_body(issue)
        cmd = [
            GH,
            "issue",
            "create",
            "--repo",
            REPO,
            "--title",
            issue["title"],
            "--body",
            body,
            "--label",
            issue["label"],
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, check=True)
        url = result.stdout.strip()
        print(f"#{num:3d} [{issue['label']:17s}] {url}")


if __name__ == "__main__":
    main()
