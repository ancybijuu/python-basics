# ==========================================
# DAY 4 - PYTHON OPERATORS
# Practice Programs
# ==========================================


# 1. SIMPLE CALCULATOR
def simple_calculator():
    print("\n===== 1. SIMPLE CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
            return
        result = num1 / num2
    else:
        print("Invalid operator.")
        return

    print("Result:", result)


# 2. EVEN OR ODD
def even_or_odd():
    print("\n===== 2. EVEN OR ODD =====")

    number = int(input("Enter a number: "))

    if number % 2 == 0:
        print(number, "is Even")
    else:
        print(number, "is Odd")


# 3. POSITIVE OR NEGATIVE
def positive_or_negative():
    print("\n===== 3. POSITIVE OR NEGATIVE =====")

    number = float(input("Enter a number: "))

    if number > 0:
        print("Positive number")
    elif number < 0:
        print("Negative number")
    else:
        print("The number is Zero")


# 4. SQUARE AND CUBE
def square_and_cube():
    print("\n===== 4. SQUARE AND CUBE =====")

    number = float(input("Enter a number: "))

    square = number ** 2
    cube = number ** 3

    print("Square:", square)
    print("Cube:", cube)


# 5. COMPARE TWO NUMBERS
def compare_numbers():
    print("\n===== 5. COMPARE TWO NUMBERS =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if num1 > num2:
        print(num1, "is greater than", num2)
    elif num2 > num1:
        print(num2, "is greater than", num1)
    else:
        print("Both numbers are equal.")


# 6. FIND REMAINDER
def find_remainder():
    print("\n===== 6. FIND REMAINDER =====")

    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))

    if num2 == 0:
        print("Cannot divide by zero.")
    else:
        remainder = num1 % num2
        print("Remainder:", remainder)


# 7. SHOPPING TOTAL
def shopping_total():
    print("\n===== 7. SHOPPING TOTAL =====")

    product = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    total = price * quantity

    print("\n----- SHOPPING DETAILS -----")
    print("Product:", product)
    print("Price:", price)
    print("Quantity:", quantity)
    print("Total:", total)


# 8. STUDENT AVERAGE
def student_average():
    print("\n===== 8. STUDENT AVERAGE =====")

    name = input("Enter student name: ")

    mark1 = float(input("Enter mark 1: "))
    mark2 = float(input("Enter mark 2: "))
    mark3 = float(input("Enter mark 3: "))
    mark4 = float(input("Enter mark 4: "))
    mark5 = float(input("Enter mark 5: "))

    total = mark1 + mark2 + mark3 + mark4 + mark5
    average = total / 5

    print("\n----- STUDENT RESULT -----")
    print("Student Name:", name)
    print("Total Marks:", total)
    print("Average:", average)


# 9. EMPLOYEE SALARY
def employee_salary():
    print("\n===== 9. EMPLOYEE SALARY =====")

    name = input("Enter employee name: ")
    basic_salary = float(input("Enter basic salary: "))
    bonus = float(input("Enter bonus: "))

    total_salary = basic_salary + bonus

    print("\n----- EMPLOYEE SALARY -----")
    print("Employee Name:", name)
    print("Basic Salary:", basic_salary)
    print("Bonus:", bonus)
    print("Total Salary:", total_salary)


# 10. ELECTRICITY BILL
def electricity_bill():
    print("\n===== 10. ELECTRICITY BILL =====")

    units = float(input("Enter electricity units: "))
    rate = float(input("Enter rate per unit: "))

    bill = units * rate

    print("\n----- ELECTRICITY BILL -----")
    print("Units:", units)
    print("Rate per Unit:", rate)
    print("Total Bill:", bill)


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("=" * 45)
    print("       DAY 4 - PRACTICE PROGRAMS")
    print("=" * 45)

    print("1. Simple Calculator")
    print("2. Even or Odd")
    print("3. Positive or Negative")
    print("4. Square and Cube")
    print("5. Compare Two Numbers")
    print("6. Find Remainder")
    print("7. Shopping Total")
    print("8. Student Average")
    print("9. Employee Salary")
    print("10. Electricity Bill")
    print("0. Exit")

    print("=" * 45)

    choice = input("Enter your choice: ")

    if choice == "1":
        simple_calculator()

    elif choice == "2":
        even_or_odd()

    elif choice == "3":
        positive_or_negative()

    elif choice == "4":
        square_and_cube()

    elif choice == "5":
        compare_numbers()

    elif choice == "6":
        find_remainder()

    elif choice == "7":
        shopping_total()

    elif choice == "8":
        student_average()

    elif choice == "9":
        employee_salary()

    elif choice == "10":
        electricity_bill()

    elif choice == "0":
        print("\nThank you for practicing Python!")
        print("Day 4 completed! 🚀")
        break

    else:
        print("\nInvalid choice. Please try again.")