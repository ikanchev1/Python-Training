student_scores = {
'Ivan': 5.00,
'Alex': 3.50,
'Maria': 5.50,
'Georgy': 5.00
}

best_student_scores = {}

for k, v in student_scores.items():
    if v > 4.00:
        best_student_scores[k] = [v]

for k in best_student_scores.keys():
    print(k)
