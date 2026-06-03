
# Function to get all unique conditions from the list of patients
def get_all_conditions(patients):
    # use a list to store unique conditions
    conditions = []  
    for patient in patients:
        if patient['condition'] not in conditions:  
            conditions.append(patient['condition'])  
    return conditions  

patients = [{'name':'A','age':30,'condition':'Malaria','status':'admitted'},{'name':'B','age':25,'condition':'Malaria','status':'admitted'},{'name':'C','age':40,'condition':'Flu','status':'admitted'}]

if __name__ == "__main__":
    try:
        print(get_all_conditions(patients))  
    except Exception as e:
        print(f"An error occurred: {e}")
