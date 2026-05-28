def create_patient(name, age, condition, status="admitted"):
    return {
        "name": name,
        "age": age,
        "condition": condition,
        "status": status
    }

if __name__ == "__main__":
    print(create_patient("John Otieno", 35, "Malaria"))