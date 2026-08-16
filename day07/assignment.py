# ==========================================
# DAY 7 - FUNCTION ASSIGNMENT
# ==========================================


# 1. Check positive or negative

def check_number(number):

    if number > 0:
        return "Positive"

    elif number < 0:
        return "Negative"

    return "Zero"


number = int(input("Enter a number: "))

print(check_number(number))


# 2. Find largest of three numbers

def largest(a, b, c):

    if a >= b and a >= c:
        return a

    elif b >= a and b >= c:
        return b

    return c


print("Largest:", largest(10, 50, 30))


# 3. Calculate simple interest

def simple_interest(principal, rate, time):
    return (principal * rate * time) / 100


print("Simple Interest:", simple_interest(10000, 5, 2))


# 4. Calculate rectangle area

def rectangle_area(length, width):
    return length * width


print("Rectangle Area:", rectangle_area(10, 5))


# 5. Calculate circle area

def circle_area(radius):

    pi = 3.14159

    return pi * radius * radius


print("Circle Area:", circle_area(7))


# 6. Check prime number

def is_prime(number):

    if number <= 1:
        return False

    for i in range(2, number):

        if number % i == 0:
            return False

    return True


number = int(input("Enter number: "))

if is_prime(number):
    print("Prime number")

else:
    print("Not a prime number")


# 7. Calculate factorial

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


number = int(input("Enter number: "))

print("Factorial:", factorial(number))


# 8. Convert Celsius to Fahrenheit

def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


temperature = float(input("Enter Celsius: "))

print("Fahrenheit:", celsius_to_fahrenheit(temperature))


# 9. Calculate percentage

def percentage(total, obtained):

    return (obtained / total) * 100


print("Percentage:", percentage(500, 425))


# 10. Calculate employee salary

def calculate_salary(basic, allowance, bonus):

    return basic + allowance + bonus


salary = calculate_salary(25000, 5000, 3000)

print("Total Salary:", salary)