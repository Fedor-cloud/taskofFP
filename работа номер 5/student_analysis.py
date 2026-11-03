from functools import reduce

FEDOS_MAK_STUDENTS = [
    {"name": "Анна", "age": 20, "grade": 4.5},
    {"name": "Борис", "age": 22, "grade": 3.8},
    {"name": "Виктор", "age": 19, "grade": 4.2},
    {"name": "Галина", "age": 21, "grade": 4.9},
    {"name": "Дмитрий", "age": 23, "grade": 3.5}
]

FEDOS_MAK_FORMAT_STUDENTS = lambda students: list(
    map(
        lambda student: (
            f"Имя: {student['name']}, Оценка: {student['grade']}"
        ),
        students
    )
)


FEDOS_MAK_FILTER_HIGH_GRADE = lambda threshold: lambda students: list(
    filter(
        lambda student: student["grade"] > threshold,
        students
    )
)

FEDOS_MAK_AVERAGE_AGE = lambda age_key: lambda students: (
    None
    if not students
    else reduce(
        lambda total, student: total + student[age_key],
        students,
        0
    ) / len(students)
)


print("Строки со студентами:", FEDOS_MAK_FORMAT_STUDENTS(FEDOS_MAK_STUDENTS))
print("Студенты с оценкой выше 4.0:", FEDOS_MAK_FILTER_HIGH_GRADE(4.0)(FEDOS_MAK_STUDENTS))
print(
    "Средний возраст отобранных студентов:",
    FEDOS_MAK_AVERAGE_AGE("age")(
        FEDOS_MAK_FILTER_HIGH_GRADE(4.0)(FEDOS_MAK_STUDENTS)
    )
)

# начиная с 30 по 35 строчку что за оператор как называется - будет ответ работа защищена 
#print(
#    "До переназначения функция возвращает:",
#    FEDOS_MAK_FILTER_HIGH_GRADE(4.0)(FEDOS_MAK_STUDENTS)
#)

#FEDOS_MAK_FILTER_HIGH_GRADE = 0

#print("После переназначения имя хранит:", FEDOS_MAK_FILTER_HIGH_GRADE)

#try:
#    FEDOS_MAK_FILTER_HIGH_GRADE(4.0)(FEDOS_MAK_STUDENTS)
#except TypeError as error:
#    print("Вызвать имя как функцию нельзя:", error)
