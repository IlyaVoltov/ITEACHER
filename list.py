# Чтение данных из файла
with open('input.txt', 'r', encoding='utf-8') as infile:
    lines = infile.readlines()

# Переменные для подсчёта сумм оценок и количества учеников
math_sum = 0
physics_sum = 0
russian_sum = 0
num_students = 0

# Открытие выходного файла для записи
with open('output.txt', 'w', encoding='utf-8') as outfile:
    for line in lines:
        # Разделяем строку на фамилию и оценки
        parts = line.strip().split(';')
        surname = parts[0]
        math, physics, russian = map(int, parts[1:4])

        # Рассчитываем среднюю оценку для абитуриента
        average = (math + physics + russian) / 3

        # Записываем средний балл с точностью до 9 знаков
        outfile.write(f'{average:.9f}\n')

        # Суммируем оценки по предметам
        math_sum += math
        physics_sum += physics
        russian_sum += russian
        num_students += 1

    # Рассчитываем средние оценки по предметам
    math_avg = math_sum / num_students
    physics_avg = physics_sum / num_students
    russian_avg = russian_sum / num_students

    # Записываем итоговую строку с общими средними баллами
    outfile.write(f'{math_avg:.9f} {physics_avg:.9f} {russian_avg:.9f}')
