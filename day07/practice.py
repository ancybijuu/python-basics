# ==========================================
# DAY 7 - FUNCTION PRACTICE
# ==========================================


# 1. Greeting function

def greet(name):
    print("Hello", name)


greet("Ancy")


# 2. Add two numbers

def add(a, b):
    return a + b


print("Sum:", add(10, 20))


# 3. Subtract two numbers

def subtract(a, b):
    return a - b


print("Difference:", subtract(50, 20))


# 4. Check even or odd

def check_even_odd(number):

    if number % 2 == 0:
        return "Even"

    return "Odd"


print("Number is:", check_even_odd(15))


# 5. Find square

def square(number):
    return number * number


print("Square:", square(8))


# 6. Find cube

def cube(number):
    return number ** 3


print("Cube:", cube(4))


# 7. Find largest number

def largest(a, b):

    if a > b:
        return a

    return b


print("Largest:", largest(50, 30))


# 8. Calculate area of rectangle

def rectangle_area(length, width):
    return length * width


print("Area:", rectangle_area(10, 5))


# 9. Calculate average

def average(a, b, c):
    return (a + b + c) / 3


print("Average:", average(80, 70, 90))


# 10. Calculate factorial

def factorial(number):

    result = 1

    for i in range(1, number + 1):
        result *= i

    return result


print("Factorial:", factorial(5))