# ==========================================
# DAY 5 - MINI PROJECT
# STUDENT RESULT SYSTEM
# ==========================================


print("=" * 45)
print("          STUDENT RESULT SYSTEM")
print("=" * 45)


# Student Information

student_name = input("Enter student name: ")
roll_number = input("Enter roll number: ")
department = input("Enter department: ")


# Subject Marks

python_mark = float(input("Enter Python mark: "))
html_mark = float(input("Enter HTML mark: "))
css_mark = float(input("Enter CSS mark: "))


# Validate Marks

if (
    python_mark < 0 or python_mark > 100
    or html_mark < 0 or html_mark > 100
    or css_mark < 0 or css_mark > 100
):
    print("\nInvalid marks!")
    print("Marks must be between 0 and 100.")

else:

    # Calculate Total

    total = python_mark + html_mark + css_mark

    # Calculate Average

    average = total / 3


    # Calculate Grade

    if average >= 90:
        grade = "A+"

    elif average >= 80:
        grade = "A"

    elif average >= 70:
        grade = "B"

    elif average >= 60:
        grade = "C"

    elif average >= 50:
        grade = "D"

    else:
        grade = "F"


    # Calculate Result

    if (
        python_mark >= 40
        and html_mark >= 40
        and css_mark >= 40
    ):
        result = "PASS"
    else:
        result = "FAIL"


    # Display Result

    print("\n")
    print("=" * 45)
    print("             STUDENT RESULT")
    print("=" * 45)

    print("Student Name :", student_name)
    print("Roll Number  :", roll_number)
    print("Department   :", department)

    print("-" * 45)

    print("Python       :", python_mark)
    print("HTML         :", html_mark)
    print("CSS          :", css_mark)

    print("-" * 45)

    print("Total        :", total)
    print("Average      :", round(average, 2))
    print("Grade        :", grade)
    print("Result       :", result)

    print("=" * 45)

    if result == "PASS":
        print("🎉 Congratulations! You passed.")
    else:
        print("Better luck next time. Keep practicing!")

    print("=" * 45)