#подсчет букв в строке
s = input()

def count_and_print_in_line(s):
    d = {}
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    for i in sorted(d):
        print(i, d[i], end=' ')


count_and_print_in_line(s)