import secrets
import string

def generate_password(min_length=8, max_length=32):
    # Определим возможные символы для пароля
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation
    # Объединим все возможные символы
    all_characters = lowercase_letters + uppercase_letters + digits + special_characters
    # Случайная длина пароля в заданном диапазоне
    password_length = secrets.randbelow(max_length - min_length + 1) + min_length
    # Генерация пароля
    password = ''.join(secrets.choice(all_characters) for _ in range(password_length))
    return password

print("Generated password:", generate_password())
