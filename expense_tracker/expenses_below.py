def below_expense(exp, amount):
    for i in exp:
        if i['amount'] < amount:
            print(i)

expenses = [
    {'desc': 'A', 'amount': 100, 'category': 'food'},
    {'desc': 'B', 'amount': 50, 'category': 'food'},
    {'desc': 'C', 'amount': 200, 'category': 'bills'}
]

below_expense(expenses,200)

