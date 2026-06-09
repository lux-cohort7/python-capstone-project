# Write a function that finds a student by name and updates their score and grade. Return the updated list.
# - Issue 19

students = [{"name": "Amina", "score": 55, "grade": "C"}]


def update_score(students, name, score):
    for s in students:
        if s["name"].lower() == name.lower():
            s["score"] = score
            if s["score"] >= 80:
                s["grade"] = "A"
            elif s["score"] >= 60:
                s["grade"] = "B"
            elif s["score"] >= 50:
                s["grade"] = "C"
            elif s["score"] >= 40:
                s["grade"] = "D"
            else:
                s["grade"] = "E"
    return students


print(update_score(students, "Amina", 90))
