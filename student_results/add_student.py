# Write a function that takes a list of student dicts, a name, and a score.
# Creates a student dict and appends it to the list. Return the updated list.

students = []


def add_student(students, name, score):
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    students.append({"name": name, "score": score, "grade": grade})
    return students


print(add_student(students, "Brian", 72))
# Expected output: [{"name": "Brian", "score": 72, "grade": "C"}]
