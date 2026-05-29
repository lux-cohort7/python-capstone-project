# Write a function that prints each patient neatly: '1. John Otieno | Age: 35 | Malaria | admitted'

patients = [{'name':'John Otieno','age':35,'condition':'Malaria','status':'admitted'}]

def list_patients(patients):
    '''Prints a list of patients in a neat format.'''
    for index, patient in enumerate(patients, start=1):
        name, age, condition, status = patient["name"], patient["age"], patient["condition"], patient["status"]
        print(f"{index}. {name} | Age: {age} | {condition} | {status}")
    return(patients)
list_patients(patients)
