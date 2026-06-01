patients = [{'name':'John','age':35,'condition':'Malaria','status':'admitted'}
            ,{'name':'Jane','age':28,'condition':'Flu','status':'discharged'}]
print(get_discharged(patients))


# define the function that accepts the patients list
def get_discharged(patients):
    discharged = [] # creation of empty list

# a for loop for each patient
    for patient in patients:
        if patient['status'] == 'discharged': # check for status of patient
            discharged.append(patient)
    return discharged # send the final list as output
