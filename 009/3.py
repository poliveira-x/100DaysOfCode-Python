student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}


student_grades = {}



for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "Outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "Excceded expectations"
    elif student_scores[i] > 70:
        student_grades[i] = "Good"
    else:
        student_grades[i] = "Fail"


print(f"\n\n{student_scores}")
print(f"\n{student_grades}\n")



