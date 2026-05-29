def update_condition(patients, name, new_condition):
    """
    Task description
    Write a function that updates a patient's condition by name. Return updated list.
    """
    for patient in patients:
        if patient["name"] == name:
            patient["condition"] = new_condition
            # print(patient)
    
    return patients


patients = [
    {'name': "John", 'age': 35, 'condition': "Malaria", 'status': "admitted"}
]

print(update_condition(patients,'John','Typhoid')[0]['condition'])
