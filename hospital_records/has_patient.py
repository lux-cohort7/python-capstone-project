# issue-111/has-patient
# Write a function that returns True if a patient with the given name exists.

def has_patient(patients, name):
    for patient in patients:
      if patient['name'] == name:
        return True
    return False

patients = [{'name':'John','age':35,'condition':'Malaria','status':'admitted'}]

if __name__ == "__main__":
    print(has_patient(patients,'John'))
    print(has_patient(patients,'Mary'))