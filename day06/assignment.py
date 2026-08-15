# ==========================================
# DAY 6 - PYTHON LOOPS
# ASSIGNMENT
# ==========================================


# 1. PRINT 1 TO 100

print("\n===== 1. NUMBERS 1 TO 100 =====")

for i in range(1, 101):
    print(i)


# 2. EVEN NUMBERS 1 TO 100

print("\n===== 2. EVEN NUMBERS =====")

for i in range(1, 101):

    if i % 2 == 0:
        print(i)


# 3. ODD NUMBERS 1 TO 100

print("\n===== 3. ODD NUMBERS =====")

for i in range(1, 101):

    if i % 2 != 0:
        print(i)


# 4. MULTIPLICATION TABLE

print("\n===== 4. MULTIPLICATION TABLE =====")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 5. SUM OF NUMBERS

print("\n===== 5. SUM OF NUMBERS =====")

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# 6. FACTORIAL

print("\n===== 6. FACTORIAL =====")

number = int(input("Enter a number: "))

if number < 0:

    print("Factorial is not possible for negative numbers.")

else:

    factorial = 1

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)


# 7. REVERSE A NUMBER

print("\n===== 7. REVERSE NUMBER =====")

number = int(input("Enter a number: "))

original = number
reverse = 0

number = abs(number)

while number > 0:

    digit = number % 10

    reverse = reverse * 10 + digit

    number //= 10


if original < 0:
    reverse = -reverse

print("Reverse:", reverse)


# 8. COUNT DIGITS

print("\n===== 8. COUNT DIGITS =====")

number = int(input("Enter a number: "))

number = abs(number)

if number == 0:

    digit_count = 1

else:

    digit_count = 0

    while number > 0:

        number //= 10

        digit_count += 1

print("Number of digits:", digit_count)


# 9. PRIME NUMBER

print("\n===== 9. PRIME NUMBER =====")

number = int(input("Enter a number: "))

if number <= 1:

    print(number, "is not a prime number.")

else:

    is_prime = True

    for i in range(2, number):

        if number % i == 0:

            is_prime = False
            break

    if is_prime:
        print(number, "is a prime number.")

    else:
        print(number, "is not a prime number.")


# 10. FIBONACCI SERIES

print("\n===== 10. FIBONACCI SERIES =====")

terms = int(input("Enter number of terms: "))

first = 0
second = 1

if terms <= 0:

    print("Enter a positive number.")

else:

    print("Fibonacci Series:")

    for i in range(terms):

        print(first, end=" ")

        next_number = first + second

        first = second
        second = next_number

    print()