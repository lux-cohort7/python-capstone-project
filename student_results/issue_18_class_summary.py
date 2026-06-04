students = [
    {"name": "Monicah Kiarie", "score": 80},
    {"name": "John Wafula", "score": 40},
    {"name": "Lawrence Baraki", "score": 65},
    {"name": "Nancy Wakonyo", "score": 90},
]

def get_class_summary(students):

  """ The function is used to get the students 
  summary as a dictionary when called """

  total = len(students)
  passed = 0
  failed = 0
  scores_total = 0

# Loop through all students

  for student in students:
    score = student["score"]
    scores_total += score

    if score >= 50:
      passed += 1
    else:
      failed += 1
    
    average = round(scores_total / total, 2)

  return{
      "Total": total,
      "Passed": passed,
      "Failed": failed,
      "Average": average
}

print(get_class_summary(students))
