students_count = int(input("Введите количество учеников: "))
students = {}

for _ in range(students_count):
    name = input("Имя ученика: ")
    subjects_scores = input("Введите предметы и оценки через запятую (например, Математика:5, Физика:4): ")
    subjects_scores_dict = {}

    for item in subjects_scores.split(', '):
        subject, score = item.split(':')
        subjects_scores_dict[subject] = int(score)

    students[name] = subjects_scores_dict

print("Список учеников с их оценками:", students)

best_student = ""
highest_average = 0

for name in students:
    scores = students[name].values()
    average_score = sum(scores) / len(scores)
    print(f"{name}: средняя оценка {average_score:.1f}")

    if average_score > highest_average:
        highest_average = average_score
        best_student = name

print(f"Лучший ученик: {best_student} (средняя оценка {highest_average:.1f})")
