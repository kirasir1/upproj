import pandas as pd
from datetime import datetime

students = [
    {
        "name": "Иванов Иван",
        "date_of_birth": "1999-03-12",
        "exam_book": [
            {"subject": "Математика", "exam_date": "2023-06-15", "teacher": "Петров Петр Петрович"},
            {"subject": "Физика", "exam_date": "2023-07-01", "teacher": "Сидоров Сидор Сидорович"},
            {"subject": "Химия", "exam_date": "2023-08-01", "teacher": "Кузнецов Алексей Викторович"}
        ]
    },
    {
        "name": "Петров Петр",
        "date_of_birth": "1998-07-25",
        "exam_book": [
            {"subject": "Математика", "exam_date": "2023-06-15", "teacher": "Петров Петр Петрович"},
            {"subject": "Информатика", "exam_date": "2023-07-15", "teacher": "Смирнова Наталья Сергеевна"},
            {"subject": "Английский", "exam_date": "2023-09-01", "teacher": "Иванова Анна Викторовна"}
        ]
    }
]

exam_dates = []

for student in students:
    for exam in student["exam_book"]:
        exam_dates.append({
            "Дата экзамена": exam["exam_date"],
            "Предмет": exam["subject"],
            "Студент": student["name"],
            "Преподаватель": exam["teacher"]
        })

exam_dates_df = pd.DataFrame(exam_dates)
unique_exam_dates_df = exam_dates_df.drop_duplicates(subset=["Дата экзамена"])
sorted_unique_exam_dates_df = unique_exam_dates_df.sort_values(by="Дата экзамена")
print(sorted_unique_exam_dates_df)
