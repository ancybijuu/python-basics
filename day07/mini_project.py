# ==========================================
# DAY 7 MINI PROJECT
# STUDENT GRADE CALCULATOR
# ==========================================


def calculate_total(marks):

    return sum(marks)


def calculate_average(marks):

    return sum(marks) / len(marks)


def calculate_grade(average):

    if average >= 90:
        return "A+"

    elif average >= 80:
        return "A"

    elif average >= 70:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 50:
        return "D"

    else:
        return "F"


def check_result(marks):

    for mark in marks:

        if mark < 40:
            return "FAIL"

    return "PASS"


print("=" * 45)
print("       STUDENT GRADE CALCULATOR")
print("=" * 45)


name = input("Enter student name: ")
roll_number = input("Enter roll number: ")

print("\nEnter marks for 5 subjects:")

python_mark = float(input("Python: "))
html_mark = float(input("HTML: "))
css_mark = float(input("CSS: "))
database_mark = float(input("Database: "))
django_mark = float(input("Django: "))


marks = [
    python_mark,
    html_mark,
    css_mark,
    database_mark,
    django_mark
]


total = calculate_total(marks)

average = calculate_average(marks)

grade = calculate_grade(average)

result = check_result(marks)


print("\n" + "=" * 45)
print("           STUDENT REPORT")
print("=" * 45)

print("Name       :", name)
print("Roll Number:", roll_number)

print("-" * 45)

print("Python     :", python_mark)
print("HTML       :", html_mark)
print("CSS        :", css_mark)
print("Database   :", database_mark)
print("Django     :", django_mark)

print("-" * 45)

print("Total      :", total)
print("Average    :", round(average, 2))
print("Grade      :", grade)
print("Result     :", result)

print("=" * 45)