def format_student_report(student):
    score = student.get('score', 0)
    if score >= 90:
        grade, remark = 'A', 'Excellent'
    elif score >= 80:
        grade, remark = 'B', 'Good'
    elif score >= 70:
        grade, remark = 'C', 'Satisfactory'
    else:
        grade, remark = 'F', 'Needs Improvement'
        
    return (
        f"Name: {student.get('name', 'N/A')} | "
        f"Score: {score}/100 | "
        f"Grade: {student.get('grade', grade)} | "
        f"Remark: {student.get('remark', remark)}"
    )
print(format_student_report({'name':'Amina','score':88,'grade':'B'}))
