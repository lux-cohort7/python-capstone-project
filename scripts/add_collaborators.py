"""
Add GitHub collaborators from a Google Forms CSV export.

Export form responses: Google Form → Responses → ⋮ → Download responses (.csv)
Save as: scripts/collaborators.csv

Expected columns (names are flexible):
  - GitHub Username (required)
  - Name, Github Email (optional, for logging)

Usage:
  python scripts/add_collaborators.py
  python scripts/add_collaborators.py --dry-run
  python scripts/add_collaborators.py --permission push
"""
from __future__ import annotations

import argparse
import csv
import re
import subprocess
import sys
import time
from pathlib import Path

GH = r"C:\Program Files\GitHub CLI\gh.exe"
REPO = "lux-cohort7/python-capstone-project"
ORG = "lux-cohort7"
DEFAULT_CSV = Path(__file__).resolve().parent / "collaborators.csv"

USERNAME_KEYS = (
    "github username",
    "github_username",
    "github user",
    "username",
    "github",
)
NAME_KEYS = ("name", "full name", "student name")
EMAIL_KEYS = ("github email", "github_email", "email")


def normalize_header(h: str) -> str:
    return re.sub(r"\s+", " ", h.strip().lower())


def pick_column(fieldnames: list[str], candidates: tuple[str, ...]) -> str | None:
    normalized = {normalize_header(f): f for f in fieldnames if f}
    for key in candidates:
        if key in normalized:
            return normalized[key]
    for norm, original in normalized.items():
        for key in candidates:
            if key in norm:
                return original
    return None


def clean_username(raw: str) -> str | None:
    if not raw:
        return None
    u = raw.strip().lstrip("@")
    if not u or u.lower() in ("n/a", "na", "none", "-", ""):
        return None

    # https://github.com/username or github.com/username
    url_match = re.search(r"github\.com/([a-zA-Z0-9](?:[a-zA-Z0-9-]{0,37}[a-zA-Z0-9])?)", u, re.I)
    if url_match:
        return url_match.group(1)

    # Remove wrapping parentheses: (stephenomengo)
    u = u.strip("()")

    # profile paths: user/repo → take first segment only
    if "/" in u:
        u = u.split("/")[0].strip()

    # spaces → hyphens (GitHub usernames cannot contain spaces)
    u = re.sub(r"\s+", "-", u.strip())

    # trim invalid edge hyphens
    u = u.strip("-")

    if not u or u.lower() in ("n/a", "na", "none"):
        return None
    if not re.match(r"^[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,37}[a-zA-Z0-9])?$", u):
        # allow single-char? no. allow trailing hyphen users: relax end check
        if re.match(r"^[a-zA-Z0-9][a-zA-Z0-9-]{0,38}$", u):
            return u.rstrip("-") or None
        return None
    return u


def load_rows(csv_path: Path) -> list[dict]:
    with csv_path.open(newline="", encoding="utf-8-sig") as f:
        reader = csv.DictReader(f)
        if not reader.fieldnames:
            raise SystemExit(f"No headers in {csv_path}")
        user_col = pick_column(list(reader.fieldnames), USERNAME_KEYS)
        if not user_col:
            raise SystemExit(
                f"Could not find GitHub Username column. Headers: {reader.fieldnames}"
            )
        name_col = pick_column(list(reader.fieldnames), NAME_KEYS)
        email_col = pick_column(list(reader.fieldnames), EMAIL_KEYS)

        rows = []
        seen: set[str] = set()
        for i, row in enumerate(reader, start=2):
            username = clean_username(row.get(user_col, ""))
            if not username:
                print(f"  skip row {i}: empty/invalid username", file=sys.stderr)
                continue
            if username.lower() in seen:
                print(f"  skip row {i}: duplicate @{username}", file=sys.stderr)
                continue
            seen.add(username.lower())
            rows.append(
                {
                    "username": username,
                    "name": (row.get(name_col, "") if name_col else "").strip(),
                    "email": (row.get(email_col, "") if email_col else "").strip(),
                }
            )
        return rows


def add_collaborator(username: str, permission: str, dry_run: bool) -> tuple[bool, str]:
    if dry_run:
        return True, "dry-run"
    cmd = [
        GH,
        "api",
        "--method",
        "PUT",
        f"repos/{REPO}/collaborators/{username}",
        "-f",
        f"permission={permission}",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return True, "invited"
    err = (result.stderr or result.stdout).strip()
    return False, err


def add_team_member(username: str, team: str, dry_run: bool) -> tuple[bool, str]:
    if dry_run:
        return True, "dry-run team"
    cmd = [
        GH,
        "api",
        "--method",
        "PUT",
        f"orgs/{ORG}/teams/{team}/memberships/{username}",
        "-f",
        "role=member",
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        return True, "added to team"
    err = (result.stderr or result.stdout).strip()
    # Already on team or pending org invite is fine
    if "already" in err.lower():
        return True, "already on team"
    return False, err


def main() -> None:
    parser = argparse.ArgumentParser(description="Add repo collaborators from CSV")
    parser.add_argument(
        "--csv",
        type=Path,
        default=DEFAULT_CSV,
        help=f"Path to CSV (default: {DEFAULT_CSV})",
    )
    parser.add_argument(
        "--permission",
        default="push",
        choices=["pull", "triage", "push", "maintain", "admin"],
        help="Collaborator permission (default: push — can clone, branch, push, open PRs)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print usernames only, do not invite",
    )
    parser.add_argument(
        "--delay",
        type=float,
        default=2.0,
        help="Seconds to wait between invites (avoids GitHub rate limit, default: 2)",
    )
    parser.add_argument(
        "--team",
        default="students",
        help="Org team slug to add members to after invite (default: students)",
    )
    parser.add_argument(
        "--skip-team",
        action="store_true",
        help="Only repo collaborator invite, do not add to org team",
    )
    args = parser.parse_args()

    if not args.csv.exists():
        raise SystemExit(
            f"CSV not found: {args.csv}\n\n"
            "Export Google Form responses:\n"
            "  Form → Responses tab → ⋮ (three dots) → Download responses (.csv)\n"
            f"  Save as: {DEFAULT_CSV}"
        )

    rows = load_rows(args.csv)
    if not rows:
        raise SystemExit("No valid GitHub usernames found in CSV.")

    print(f"Found {len(rows)} unique username(s) in {args.csv}")
    if args.dry_run:
        print("(dry-run — no invites sent)\n")

    ok, fail = 0, 0
    for i, row in enumerate(rows):
        u = row["username"]
        label = f"@{u}"
        if row["name"]:
            label += f" ({row['name']})"
        success, msg = add_collaborator(u, args.permission, args.dry_run)
        if success and not args.skip_team and args.team:
            team_ok, team_msg = add_team_member(u, args.team, args.dry_run)
            if team_ok:
                msg = f"{msg}; {team_msg}"
            else:
                msg = f"{msg}; team: {team_msg}"
        if success:
            ok += 1
            print(f"  OK  {label} — {msg}")
        else:
            fail += 1
            print(f"  FAIL {label} — {msg}")
        if not args.dry_run and i < len(rows) - 1 and args.delay > 0:
            time.sleep(args.delay)

    print(f"\nDone: {ok} ok, {fail} failed")
    if fail:
        sys.exit(1)


if __name__ == "__main__":
    main()
