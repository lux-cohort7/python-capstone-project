def readmit_patient(patients, name):
    """
    Finds a patient by name and changes their status from 'discharged' to 'admitted'.
    Returns the updated list of patients.
    """
    for patient in patients:
        if patient.get("name").lower() == name.lower():
            # Update status only if they are currently discharged
            if patient.get("status") == "discharged":
                patient["status"] = "admitted"
            break
    return patients


# Test data
patients = [{"name": "John", "age": 35, "condition": "Malaria", "status": "discharged"}]


if __name__ == "__main__":
    print(
        readmit_patient(patients, "John")[0]["status"]
    )  # -- Expected outcome: admitted
