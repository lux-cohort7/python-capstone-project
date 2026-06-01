patients = [
    {"name": "John", "age": 35, "condition": "Malaria", "status": "admitted"},
    {"name": "Jane", "age": 28, "condition": "Flu", "status": "discharged"},
]

def get_admitted(patients):
    for p in patients:
        if p["status"] == "admitted":
            print(f'Patient(s) with admitted status: {p["name"]}')

get_admitted(patients)
