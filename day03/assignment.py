# ==========================================
# Day 3 - Assignment
# ==========================================

print("=" * 50)
print("        DAY 3 ASSIGNMENT")
print("=" * 50)


# 1. Add Two Numbers
print("\n1. ADD TWO NUMBERS")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

addition = num1 + num2

print("Addition:", addition)


# 2. Area of Rectangle
print("\n2. AREA OF RECTANGLE")

length = float(input("Enter length: "))
breadth = float(input("Enter breadth: "))

area = length * breadth

print("Area:", area)


# 3. Perimeter of Rectangle
print("\n3. PERIMETER OF RECTANGLE")

perimeter = 2 * (length + breadth)

print("Perimeter:", perimeter)


# 4. Simple Interest
print("\n4. SIMPLE INTEREST")

principal = float(input("Enter principal amount: "))
rate = float(input("Enter rate: "))
time = float(input("Enter time: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest:", simple_interest)


# 5. Celsius to Fahrenheit
print("\n5. CELSIUS TO FAHRENHEIT")

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9 / 5) + 32

print("Fahrenheit:", fahrenheit)


# 6. Kilometers to Meters
print("\n6. KILOMETERS TO METERS")

kilometers = float(input("Enter kilometers: "))

meters = kilometers * 1000

print("Meters:", meters)


# 7. Average of Three Numbers
print("\n7. AVERAGE OF THREE NUMBERS")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
c = float(input("Enter third number: "))

average = (a + b + c) / 3

print("Average:", average)


# 8. Student Report
print("\n8. STUDENT REPORT")

student_name = input("Student Name: ")
roll_number = input("Roll Number: ")

mark1 = float(input("Enter Mark 1: "))
mark2 = float(input("Enter Mark 2: "))
mark3 = float(input("Enter Mark 3: "))

total = mark1 + mark2 + mark3
average_mark = total / 3

print("\n----- STUDENT REPORT -----")
print("Name:", student_name)
print("Roll Number:", roll_number)
print("Total:", total)
print("Average:", average_mark)


# 9. Employee Salary
print("\n9. EMPLOYEE SALARY")

employee_name = input("Employee Name: ")
basic_salary = float(input("Basic Salary: "))
bonus = float(input("Bonus: "))

total_salary = basic_salary + bonus

print("\n----- SALARY DETAILS -----")
print("Employee:", employee_name)
print("Basic Salary:", basic_salary)
print("Bonus:", bonus)
print("Total Salary:", total_salary)


# 10. Personal Information Form
print("\n10. PERSONAL INFORMATION")

name = input("Name: ")
age = int(input("Age: "))
city = input("City: ")
email = input("Email: ")
course = input("Course: ")

print("\n----- PERSONAL INFORMATION -----")
print("Name:", name)
print("Age:", age)
print("City:", city)
print("Email:", email)
print("Course:", course)

print("\n" + "=" * 50)
print("       ASSIGNMENT COMPLETED")
print("=" * 50)