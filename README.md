# Учебный Проект

Данный репозиторий содержит две программы: программу для генерации безопасных паролей и программу для управления данными учебной группы.

## 1. Генератор паролей

Программа позволяет пользователю генерировать безопасные пароли с задаваемой длиной, которые включают строчные и прописные буквы, цифры и специальные символы.

### Функциональность

- Ввод пользователем желаемой длины пароля.
- Проверка корректности введенной длины (от 8 до 32 символов).
- Генерация случайного пароля с использованием криптографически безопасных методов.

### Запуск программы

Программа написана на Python и требует Python версии 3.x.

```bash
python generate_password.py
```

### Пример использования

```bash
Введите желаемую длину пароля (от 8 до 32): 12
Ваш новый пароль: A7f@1sGp9*dw
```

## 2. Управление данными учебной группы

Программа предназначена для управления данными студентов, включая информацию о предметах и датах экзаменов.
Функциональность
- Хранение информации о студентах (имя, дата рождения, зачетка с предметами).
- Вывод таблицы всех уникальных дат экзаменов студентов.

### Запуск программы

Программа написана на Python и требует Python версии 3.x и библиотеку pandas.

```bash
python manage_students.py
```

Пример вывода

```bash
Дата экзамена  Предмет        Студент       Преподаватель
2023-06-15    Математика     Иванов Иван   Петров Петр Петрович
2023-07-01    Физика         Иванов Иван   Сидоров Сидор Сидорович
2023-08-01    Химия          Иванов Иван   Кузнецов Алексей Викторович
...
```

## Лицензия

Этот проект распространяется под лицензией MIT.