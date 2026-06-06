def create_student(name, score):
    if score >= 90:
        grade = 'A'
    elif score >= 80:
        grade = 'B'
    elif score >= 70:
        grade = 'C'
    elif score >= 60:
        grade = 'D'
    else:
        grade = 'F'
        
    
    return{
        'name': name, 'score': score, 'grade': grade
    }
         
   
print(create_student('Amina', 88))