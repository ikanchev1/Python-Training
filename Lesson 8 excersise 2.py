student_scores = {
'Ivan': 5.00,
'Alex': 3.50,
'Maria': 5.50,
'Georgy': 5.00
}

#Example without sorting the dictionary
best_student = ['none', 0]
worst_student = ['none', 10]

for k, v in student_scores.items():
    if v > best_student[1]:
        best_student[0] = k
        best_student[1] = v

#print(f"{best_student[0]} - {best_student[1]}")

for k, v in student_scores.items():
    if v < worst_student[1]:
        worst_student[0] = k
        worst_student[1] = v

#print(f"{worst_student[0]} - {worst_student[1]}")

#Example sorting the dictionary
sorted_scores = sorted(student_scores.items(), key=lambda kv: kv[1])

print(f"{sorted_scores[-1][0]} - {sorted_scores[-1][1]}")
print(f"{sorted_scores[0][0]} - {sorted_scores[0][1]}")
