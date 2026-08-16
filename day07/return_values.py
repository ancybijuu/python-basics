# ==========================================
# RETURN VALUES
# ==========================================


def add(a, b):
    return a + b


result = add(10, 20)

print("Result:", result)


def subtract(a, b):
    return a - b


result = subtract(50, 20)

print("Subtraction:", result)


def multiply(a, b):
    return a * b


print("Multiplication:", multiply(5, 4))


def divide(a, b):

    if b == 0:
        return "Cannot divide by zero"

    return a / b


print("Division:", divide(20, 5))


# Square

def square(number):
    return number * number


print("Square:", square(6))