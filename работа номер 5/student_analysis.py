from functools import reduce

fedos_mak_students = [
    {"name": "Анна", "age": 20, "grade": 4.5},
    {"name": "Борис", "age": 22, "grade": 3.8},
    {"name": "Виктор", "age": 19, "grade": 4.2},
    {"name": "Галина", "age": 21, "grade": 4.9},
    {"name": "Дмитрий", "age": 23, "grade": 3.5}
]

fedos_mak_format_students = lambda students: list(
    map(
        lambda student: (
            f"Имя: {student['name']}, Оценка: {student['grade']}"
        ),
        students
    )
)

fedos_mak_filter_high_grade = lambda students: list(
    filter(
        lambda student: student["grade"] > 4.0,
        students
    )
)

fedos_mak_average_age = lambda students: (
    None
    if not students
    else reduce(
        lambda total, student: total + student["age"],
        students,
        0
    ) / len(students)
)

print("Строки со студентами:", fedos_mak_format_students(fedos_mak_students))
print("Студенты с оценкой выше 4.0:", fedos_mak_filter_high_grade(fedos_mak_students))
print(
    "Средний возраст отобранных студентов:",
    fedos_mak_average_age(fedos_mak_filter_high_grade(fedos_mak_students))
)
