# A function to find the youngest patient in a list of patient records. 
# Returns the patient dictionary with the lowest age.

def get_youngest_patient(patients):
    if not patients:
        return None # Safety Check - Returns None if the list is empty
    
    youngest_patient =  patients[0] # Initialize with the first patient in the list as the youngest

    # Iterate through the list of patients and update the "youngest_patient" if a younger one is found
    for patient in patients:
        if patient['age'] < youngest_patient['age']:
            youngest_patient = patient
    return youngest_patient


# =============================================================
# Test block
# Run this block to test the function.

if __name__ == "__main__":
    # Test case 1: Basic test with two patients
    patients = [
        {'name':'John','age':35,'condition':'Malaria','status':'admitted'},
        {'name':'Baby A','age':1,'condition':'Fever','status':'admitted'}
        ]
print(get_youngest_patient(patients)['name'])
# Expected output: 'Baby A'