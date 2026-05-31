def get_oldest_patient(patients):
    """Return the patient dict with the highest age."""
    oldest = patients[0]
    for patient in patients:
        if patient['age'] > oldest['age']:
            oldest = patient
    return oldest


if __name__ == "__main__":
    patients = [
        {'name': 'John', 'age': 35, 'condition': 'Malaria', 'status': 'admitted'},
        {'name': 'Mama Jane', 'age': 72, 'condition': 'BP', 'status': 'admitted'}
    ]
    print(get_oldest_patient(patients)['name'])  # Expected: Mama Jane