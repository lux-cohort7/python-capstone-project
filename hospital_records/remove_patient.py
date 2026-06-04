"""
Task description
Write a function that removes a patient by name. Return the updated list.
"""
# Function to remove a patient by name
def remove_patient(patients, name): # patients is a list of patient records, name is the name of the patient to remove.
    updated_patients = [patient for patient in patients if patient['name'] != name] # Create a new list of patients that does not include the patient with the specified name.
    return updated_patients #Return the updated list of patients.

# Testing the function
patients = [{'name': 'John Otieno', 'age': 35, 'condition': 'Malaria', 'status': 'admitted'},
            {'name': 'Jane', 'age': 28, 'condition': 'Flu', 'status': 'admitted'}]
updated_patients = remove_patient(patients, 'John Otieno') # remove patient with name 'John Otieno'
print("Updated Patients List:", updated_patients)

# Expected Output: Updated Patients List: [{'name': 'Jane', 'age': 28, 'condition': 'Flu', 'status': 'admitted'}]