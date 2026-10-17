# ==========================================
# DAY 5 - PYTHON CONDITIONAL STATEMENTS
# ASSIGNMENT
# ==========================================


# 1. AGE CATEGORY
def age_category():
    print("\n===== 1. AGE CATEGORY =====")

    age = int(input("Enter your age: "))

    if age < 0:
        print("Invalid age.")
    elif age <= 12:
        print("Category: Child")
    elif age <= 19:
        print("Category: Teenager")
    elif age <= 59:
        print("Category: Adult")
    else:
        print("Category: Senior Citizen")


# 2. SIMPLE CALCULATOR
def calculator():
    print("\n===== 2. SIMPLE CALCULATOR =====")

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /, %): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2
        print("Result:", result)

    elif operator == "-":
        result = num1 - num2
        print("Result:", result)

    elif operator == "*":
        result = num1 * num2
        print("Result:", result)

    elif operator == "/":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 / num2
            print("Result:", result)

    elif operator == "%":
        if num2 == 0:
            print("Cannot divide by zero.")
        else:
            result = num1 % num2
            print("Result:", result)

    else:
        print("Invalid operator.")


# 3. LARGEST OF THREE NUMBERS
def largest_of_three():
    print("\n===== 3. LARGEST OF THREE NUMBERS =====")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    num3 = float(input("Enter third number: "))

    if num1 >= num2 and num1 >= num3:
        largest = num1
    elif num2 >= num1 and num2 >= num3:
        largest = num2
    else:
        largest = num3

    print("Largest number:", largest)


# 4. LOGIN SYSTEM
def login_system():
    print("\n===== 4. LOGIN SYSTEM =====")

    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == "admin" and password == "1234":
        print("Login successful!")
    else:
        print("Invalid username or password.")


# 5. ELECTRICITY BILL
def electricity_bill():
    print("\n===== 5. ELECTRICITY BILL =====")

    units = float(input("Enter electricity units: "))

    if units < 0:
        print("Invalid units.")
        return

    if units <= 100:
        bill = units * 5

    elif units <= 200:
        bill = (100 * 5) + ((units - 100) * 7)

    elif units <= 300:
        bill = (100 * 5) + (100 * 7) + ((units - 200) * 10)

    else:
        bill = (
            (100 * 5)
            + (100 * 7)
            + (100 * 10)
            + ((units - 300) * 15)
        )

    print("Electricity Bill: ₹", bill)


# 6. STUDENT GRADE
def student_grade():
    print("\n===== 6. STUDENT GRADE =====")

    mark = float(input("Enter mark: "))

    if mark < 0 or mark > 100:
        print("Invalid mark. Enter a mark between 0 and 100.")

    elif mark >= 90:
        print("Grade: A+")

    elif mark >= 80:
        print("Grade: A")

    elif mark >= 70:
        print("Grade: B")

    elif mark >= 60:
        print("Grade: C")

    elif mark >= 50:
        print("Grade: D")

    else:
        print("Grade: F")


# 7. LEAP YEAR CHECKER
def leap_year():
    print("\n===== 7. LEAP YEAR CHECKER =====")

    year = int(input("Enter year: "))

    if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
        print(year, "is a leap year.")
    else:
        print(year, "is not a leap year.")


# 8. NUMBER CLASSIFICATION
def number_classification():
    print("\n===== 8. NUMBER CLASSIFICATION =====")

    number = int(input("Enter a number: "))

    if number == 0:
        print("Zero")

    elif number > 0:
        if number % 2 == 0:
            print("Positive Even")
        else:
            print("Positive Odd")

    else:
        if number % 2 == 0:
            print("Negative Even")
        else:
            print("Negative Odd")


# 9. ATM WITHDRAWAL
def atm_withdrawal():
    print("\n===== 9. ATM WITHDRAWAL =====")

    balance = float(input("Enter account balance: "))
    withdrawal = float(input("Enter withdrawal amount: "))

    if withdrawal <= 0:
        print("Invalid withdrawal amount.")

    elif withdrawal > balance:
        print("Insufficient balance.")

    else:
        remaining_balance = balance - withdrawal

        print("Withdrawal successful!")
        print("Remaining balance:", remaining_balance)


# 10. EMPLOYEE BONUS
def employee_bonus():
    print("\n===== 10. EMPLOYEE BONUS =====")

    name = input("Enter employee name: ")
    salary = float(input("Enter salary: "))
    experience = float(input("Enter years of experience: "))

    if salary < 0 or experience < 0:
        print("Invalid salary or experience.")
        return

    if experience >= 5:
        bonus_rate = 0.10

    elif experience >= 3:
        bonus_rate = 0.07

    elif experience >= 1:
        bonus_rate = 0.05

    else:
        bonus_rate = 0

    bonus = salary * bonus_rate
    final_salary = salary + bonus

    print("\n================================")
    print("       EMPLOYEE DETAILS")
    print("================================")

    print("Name         :", name)
    print("Salary       : ₹", salary)
    print("Experience   :", experience, "years")
    print("Bonus        : ₹", bonus)
    print("Final Salary : ₹", final_salary)

    print("================================")


# ==========================================
# MAIN MENU
# ==========================================

while True:

    print("\n")
    print("========================================")
    print("       DAY 5 ASSIGNMENT")
    print("========================================")

    print("1. Age Category")
    print("2. Calculator")
    print("3. Largest of Three")
    print("4. Login System")
    print("5. Electricity Bill")
    print("6. Student Grade")
    print("7. Leap Year")
    print("8. Number Classification")
    print("9. ATM Withdrawal")
    print("10. Employee Bonus")
    print("0. Exit")

    print("========================================")

    choice = input("Enter your choice: ")

    if choice == "1":
        age_category()

    elif choice == "2":
        calculator()

    elif choice == "3":
        largest_of_three()

    elif choice == "4":
        login_system()

    elif choice == "5":
        electricity_bill()

    elif choice == "6":
        student_grade()

    elif choice == "7":
        leap_year()

    elif choice == "8":
        number_classification()

    elif choice == "9":
        atm_withdrawal()

    elif choice == "10":
        employee_bonus()

    elif choice == "0":
        print("\nDay 5 Assignment Completed! 🎉")
        print("Keep learning Python! 🐍")
        break

    else:
        print("\nInvalid choice. Please enter a number from 0 to 10.")