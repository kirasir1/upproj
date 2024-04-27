import secrets
import string

def generate_password(length):
    # Определим возможные символы для пароля
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    # Объединим все возможные символы
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    # Генерация пароля указанной длины
    password = ''.join(secrets.choice(all_characters) for _ in range(length))
    return password

while True:
    try:
        password_length = int(input("Введите желаемую длину пароля (от 8 до 32): "))

        if 8 <= password_length <= 32:
            print("Generated password:", generate_password(password_length))
        else:
            print("Пожалуйста, введите число от 8 до 32.")

    except ValueError:
        print("Ошибка ввода. Пожалуйста, введите целое число.")
