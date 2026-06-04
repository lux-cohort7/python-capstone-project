def get_all_categories(expenses):
    unique_categories = set(expense['category'] for expense in expenses)
    return list(unique_categories)

expenses = [
    {'desc': 'A', 'amount': 100, 'category': 'food'},
    {'desc': 'B', 'amount': 50, 'category': 'food'},
    {'desc': 'C', 'amount': 200, 'category': 'bills'}
]

print(get_all_categories(expenses))