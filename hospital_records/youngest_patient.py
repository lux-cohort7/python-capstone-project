# A function to find the youngest patient in a list of patient records. 
# Returns the patient dictionary with the lowest age.

def get_youngest_patient(patients):
    pass


# =============================================================
# Test block
# =============================================================

if __name__ == "__main__":
    # Test case 1: Basic test with two patients
    patients = [
        {'name':'John','age':35,'condition':'Malaria','status':'admitted'},
        {'name':'Baby A','age':1,'condition':'Fever','status':'admitted'}
        ]
print(get_youngest_patient(patients)['name'])
# Expected output: 'Baby A'