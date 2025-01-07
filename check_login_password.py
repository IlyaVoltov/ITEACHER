login = input("Введите логин: ")
password = input("Введите пароль: ")

# Списки допустимых логинов и паролей
valid_logins = ["admin", "user1", "manager"]
valid_passwords = ["admin123", "pass1", "manager42"]

# Функция для проверки логина и пароля
def check_login_password(login, password, check_login=valid_logins, check_password=valid_passwords):
    if login in check_login and password in check_password:
        return True
    else:
        return False

# Вызов функции с введёнными логином и паролем
authorization = check_login_password(login, password)
print(authorization)


'''
Объяснение
valid_logins и valid_passwords — это списки с несколькими вариантами логинов и паролей.
check_login и check_password по умолчанию используют эти списки.
if login in check_login and password in check_password проверяет, входит ли введённый логин и пароль в допустимые значения.
'''