'''
Exercise 6: Student Scores Dictionary
Student: Agrim Shiwakoti
Day: 2
'''

#input values
student_scores = {
    "Agrim": 92,
    "Ram": 54,
    "Pushpa": 45,
    "Khagendra": 61,
    "Balen": 88
}

for student, score in student_scores.items():
    print(f"{student} scored: {score}")


passed_students = {student: score for student, score in student_scores.items() if score >= 60} #using comprehension

highest_score_student = max(student_scores, key=student_scores.get)

average_score = sum(student_scores.values()) / len(student_scores)

# Output
print(f"\nStudents who passed: {passed_students}")
print(f"Student with the highest score: {highest_score_student} with a score of {student_scores[highest_score_student]}")
print(f"Average score of the class: {average_score:.2f}")