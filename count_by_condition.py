patients = [
        {'name':'A','age':30,'condition':'Malaria','status':'admitted'},
        {'name':'B','age':25,'condition':'Malaria','status':'admitted'},
        {'name':'C','age':40,'condition':'Flu','status':'admitted'}
        ]
def count_by_condition(patients, condition):
    count = 0
    for patient in patients:
        if patient['condition'] == condition:
            count += 1
    return count
print("Number of patients with Malaria:")
print(count_by_condition(patients, 'Malaria'))