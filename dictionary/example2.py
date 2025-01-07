#словарь соответствия англ и русских слов - переводчик

words = {}

while True:
    s = input("Введите слово (или 'выход' для завершения): ")

    if s.lower() == 'выход':
        print("Завершаем программу...")
        break

    if s in words:
        print(f"Слово '{s}' переводится, как '{words[s]}'")
    else:
        print(f"Введите перевод слова '{s}':")
        words[s] = input()

    # Дополнительная возможность вывода всех слов в словаре
    if len(words) > 0:
        print("Текущий словарь:")
        for word, translation in words.items():
            print(f"{word}: {translation}")
