# Write a function that returns a dict where each key is a category and value is total spent in that category.

expenses = [
    {"desc": "A", "amount": 200, "category": "food"},
    {"desc": "B", "amount": 100, "category": "food"},
    {"desc": "C", "amount": 300, "category": "bills"},
]


def category_summary(expenses):
    summary = {}
    for expense in expenses:
        category = expense["category"]
        amount = expense["amount"]
        summary[category] = summary.get(category, 0) + amount
    return summary


print(category_summary(expenses))
