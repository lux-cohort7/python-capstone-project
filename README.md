# Python Capstone Project

A collaborative bootcamp capstone: **120 issues**, **5 projects**, **24 functions each**, **one student per issue**.

Repository: [github.com/Navashub/python-capstone-project](https://github.com/Navashub/python-capstone-project)

---

## Projects

| Project | Folder | Issues | Base branch |
|---------|--------|--------|-------------|
| Student Results Management | `student_results/` | [#1–#24](https://github.com/Navashub/python-capstone-project/issues?q=is%3Aissue+is%3Aopen+1..24) | `project/student-results` |
| Personal Expense Tracker | `expense_tracker/` | [#25–#48](https://github.com/Navashub/python-capstone-project/issues) | `project/expense-tracker` |
| Shop Inventory System | `shop_inventory/` | [#49–#72](https://github.com/Navashub/python-capstone-project/issues) | `project/shop-inventory` |
| Matatu Fare Calculator | `matatu_fare/` | [#73–#96](https://github.com/Navashub/python-capstone-project/issues) | `project/matatu-fare` |
| Hospital Patient Records | `hospital_records/` | [#97–#120](https://github.com/Navashub/python-capstone-project/issues) | `project/hospital-records` |

Labels on issues: `conditionals`, `loops`, `functions`, `data-structures`, `strings`

---

## One student = one issue = one file

**Do not edit `main.py` or files other students own.**

Each student creates **one new Python file** named after their function inside the correct project folder. Because every student touches a different file, pull requests merge without conflicting on the same code.

Example layout for Student Results:

```
student_results/
├── main.py                 ← do not edit (project placeholder)
├── get_grade.py            ← issue #1
├── get_grade_remark.py     ← issue #2
├── calculate_average.py    ← issue #3
├── get_highest_score.py    ← issue #4
└── ...
```

Each file contains **one function** (the one described in your issue).

### File naming rule

From the issue title **"Write `function_name`(...)"** → create **`function_name.py`**

| Issue title | Your file |
|-------------|-----------|
| Write `get_grade(score)` - return letter grade | `student_results/get_grade.py` |
| Write `create_expense(desc, amount, category)` - ... | `expense_tracker/create_expense.py` |

Use **snake_case** exactly as in the title.

---

## Step-by-step workflow

### 1. Claim an issue

1. Go to [Issues](https://github.com/Navashub/python-capstone-project/issues).
2. Pick an **open** issue in your project (or as assigned by your instructor).
3. **Comment** on the issue (e.g. “I’ll take this”) or assign yourself so two people don’t work on the same one.

### 2. Read your issue

Every issue includes:

- **Task description** - what to implement  
- **Test to run** - copy into your file or a local test block  
- **Expected output** - your code must match this  
- **Branch** - your personal branch name (e.g. `issue-01/get-grade`)  
- **Project branch** - branch you branch from and open PR into (e.g. `project/student-results`)

### 3. Clone the repo (first time only)

```bash
git clone https://github.com/Navashub/python-capstone-project.git
cd python-capstone-project
```

### 4. Check out the project branch

Use the **Project branch** shown in your issue:

```bash
git fetch origin
git checkout project/student-results
```

Replace with your project’s branch:

- `project/student-results`
- `project/expense-tracker`
- `project/shop-inventory`
- `project/matatu-fare`
- `project/hospital-records`

### 5. Create your personal branch

Use the **exact** branch name from your issue:

```bash
git checkout -b issue-01/get-grade
```

### 6. Create your function file

**Example for issue #1** (`get_grade` in Student Results):

Create `student_results/get_grade.py`:

```python
def get_grade(score):
    """Return letter grade for a score 0-100."""
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


if __name__ == "__main__":
    print(get_grade(85))  # Test from the issue — expect: B
```

Run the test locally:

```bash
python student_results/get_grade.py
```

Output must match the issue’s **Expected output**.

### 7. Commit and push

Only add **your** file:

```bash
git add student_results/get_grade.py
git commit -m "Add get_grade — closes #1"
git push -u origin issue-01/get-grade
```

Use your real path, function name, and issue number.

### 8. Open a pull request

On GitHub:

| Field | Value |
|-------|--------|
| **Base** | Project branch from your issue (e.g. `project/student-results`) |
| **Compare** | Your branch (e.g. `issue-01/get-grade`) |
| **Description** | `Closes #1` (your issue number) |

**Do not** open PRs into `main` unless your instructor says so.

### 9. Review and merge

Address review comments if any. After merge, your function is part of that project branch.

---

## Rules

1. **One issue per student** - don’t start an issue someone else claimed.  
2. **One function per file** - filename = function name + `.py`.  
3. **Don’t edit `main.py`** or another student’s `.py` file.  
4. **Branch from the project branch**, not from `main`.  
5. **Run the issue test** before opening a PR.  
6. **Never push directly** to `main` or `project/*` - always use your `issue-XX/...` branch and a PR.

---

## Quick reference (copy-paste)

Replace placeholders with your issue details.

```bash
git clone https://github.com/Navashub/python-capstone-project.git
cd python-capstone-project
git fetch origin
git checkout PROJECT_BRANCH
git checkout -b YOUR_ISSUE_BRANCH

# create PROJECT_FOLDER/FUNCTION_NAME.py and implement your function
python PROJECT_FOLDER/FUNCTION_NAME.py

git add PROJECT_FOLDER/FUNCTION_NAME.py
git commit -m "Add FUNCTION_NAME — closes #ISSUE_NUMBER"
git push -u origin YOUR_ISSUE_BRANCH
```

Then open a PR: **base** = `PROJECT_BRANCH`, **compare** = `YOUR_ISSUE_BRANCH`, body includes `Closes #ISSUE_NUMBER`.

---

## Folder map (which directory for your file)

| Issue numbers | Create your `.py` file in |
|---------------|---------------------------|
| 1–24 | `student_results/` |
| 25–48 | `expense_tracker/` |
| 49–72 | `shop_inventory/` |
| 73–96 | `matatu_fare/` |
| 97–120 | `hospital_records/` |

---

## Need help?

- Git basics: [GitHub Docs - Pull requests](https://docs.github.com/en/pull-requests)  
- Ask me or comment on your issue  

Good luck - pick an issue and ship your function.
