'''
Задача 3: Чётные числа в матрице

Сгенерируйте квадратную таблицу размером n x n (где n вводится пользователем), в которой:

Все элементы с чётной суммой индексов (i + j) равны 1,

Остальные равны 0.

'''

# Решение задачи 3
n = int(input("Введите размерность квадрата: "))

for i in range(n):  # Внешний цикл для строк
    for j in range(n):  # Внутренний цикл для столбцов
        if (i + j) % 2 == 0:  # Проверяем, чётная ли сумма индексов
            print(1, end=" ")  # Выводим 1
        else:
            print(0, end=" ")  # Выводим 0
    print()  # Переход на новую строку после каждой строки таблицы


'''
добавь к этому списку в конец последовательности слово "добавил"
'''

a = input("Введите текст: ")
words = a.split()  # Разделяем строку на список слов
words.append("добавил")  # Добавляем слово "добавил" в конец списка
print("Обновлённый список слов:", words)  # Выводим обновлённый список

'''
А теперь "достань" 2 элемент последовательности и сохрани в отдельную переменную.
'''
second_element = words.pop(1)  # Извлекаем второй элемент с помощью pop()
print("Второй элемент:", second_element)


'''
Разделение символов на группы

Дана строка s из чисел, разделённых пробелами. Сгруппируйте числа по 2 и выведите результат.
'''

s = input("Введите числа, разделённые пробелами: ")

# Разделяем строку на список чисел
numbers = s.split()

# Проверяем, что количество чисел чётное
if len(numbers) % 2 != 0:
    print("Количество чисел нечётное. Группировка невозможна.")
else:
    # Объединяем числа попарно
    grouped_numbers = [numbers[i] + numbers[i + 1] for i in range(0, len(numbers), 2)]
    # Выводим результат
    print(" ".join(grouped_numbers))


'''
Объяснение:
Сначала строка делится на список чисел с помощью split().
Проверяется, чтобы количество чисел было чётным.
Используется генератор списка для объединения чисел попарно. Например:
Индексы 0 и 1 создают группу "12".
Индексы 2 и 3 создают группу "34".
Результат выводится с помощью join(), объединяя группы через пробел.

'''

# объявление функции
def print_message():
    print('Я - Артур,')
    print('король британцев. ')


# вызов функции
print_message()

'''
звездный прямоугольник с размерами 5×7
'''
def draw_box():
    for i in range(5):
        print('*' * 7)


'''
Давайте перепишем предыдущую версию функции draw_box() так, чтобы она принимала параметры, задающие высоту и ширину прямоугольника:
'''

def draw_box(height, width):    # функция принимает два параметра
    for i in range(height):
        print('*' * width)

#Чтобы вывести звездный прямоугольник размерами 5 на 7 мы пишем код:
draw_box(5, 7)