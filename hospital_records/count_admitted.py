def count_admitted(patients):
    count = 0 # intializing total admited patients to 0 before we start counting

    for patient in patients:
        # print(patient)
        if patient.get('status') == "admitted":
            count += 1 # increment the number of admitted patient by 1 if condition is true - used get() to access the status key safely

    return count


if __name__ == "__main__":
    patients = [
        {"name": "John", "age": 35, "condition": "Malaria", "status": "admitted"},
        {"name": "Jane", "age": 28, "condition": "Flu", "status": "discharged"},
    ]

    print(count_admitted(patients))