def get_ward_report(patients):
    """Return a summary dict of patient counts by status."""
    total_patients = len(patients)
    admitted = 0
    discharged = 0
    for patient in patients:
        if patient["status"] == "admitted":
            admitted += 1
        elif patient["status"] == "discharged":
            discharged += 1
    return {
        "total_patients": total_patients,
        "admitted": admitted,
        "discharged": discharged,
    }


if __name__ == "__main__":
    patients = [{'name':'A','age':30,'condition':'Flu','status':'admitted'},{'name':'B','age':50,'condition':'BP','status':'discharged'}]
    print(get_ward_report(patients))