print("Привет, меня зовут \nЯ чат-бот, меня создал Женя.")
name = input("А как Вас зовут? - ").lower()

# Проверяем, входит ли имя в список и учитываем разные случаи
if name in ("олеся", "мама", "женя", "сергей", "папа"):
    if name == "олеся" or name == "мама":
        print("Не может быть! Вы мама моего создателя?")
        answer1 = input("да/нет - ").lower()  # Приводим ответ к нижнему регистру
        if answer1 == "да":
            print("Он столько говорил о Вас. Я рад знакомству!")
        else:
            print("Ой, простите. Я перепутал!")
    elif name == "сергей" or name == "папа":
        print("Не может быть! Вы папа моего создателя?")
        answer2 = input("да/нет - ").lower()  # Приводим ответ к нижнему регистру
        if answer2 == "да":
            print("Он столько говорил о Вас. Я рад знакомству!")
        else:
            print("Ой, простите. Я перепутал!")
    elif name == "женя":
        print("Здравствуй, создатель!")
else:
    print("Привет,", name)

print("Здорово, а Женя научил меня считать! Но пока не много, только до 10.")
count1 = int(input("Назовите число от 1 до 10 - "))

# Проверяем, входит ли число в заданный диапазон
if 0 < count1 <= 10:
    for i in range(1, count1 + 1):  # Начинаем с 1, чтобы исключить 0
        if i in (5, 6, 7, 8, 9, 10):  # Исправлено на корректное условие
            print(i, "овечек")
        elif i == 1:
            print(i, "овечка")
        elif i in (2, 3, 4):
            print(i, "овечки")
else:
    print("Я же сказал, что считаю только до 10.")

print("Кстати, я люблю играть в УГАДАЙ ЧИСЛО")
answer3 = input("Сыграем? да/нет - ").lower()

if answer3 == "да":
    print("я загадал число от 1 до 10, попробуй угадать")
    import random
    number = random.randint(1, 10)
    count2 = int(input("Введите число - "))
    while count2 != number:
        if count2 < number:
            print("слишком мало")
            count2 = int(input("Введите число - "))
        elif count2 > number:
            print("слишком много")
            count2 = int(input("Введите число - "))
    print("вы угадали!")
else:
    print("Ой, простите. Я перепутал!")

print()
print()
print("Я устал, ", name, ", я пошёл спать. До скорого!")