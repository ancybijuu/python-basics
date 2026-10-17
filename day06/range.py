# ==========================================
# DAY 6 - RANGE FUNCTION
# ==========================================


# range(stop)

print("range(5):")

for number in range(5):
    print(number)


# range(start, stop)

print("\nrange(1, 6):")

for number in range(1, 6):
    print(number)


# range(start, stop, step)

print("\nEven numbers:")

for number in range(2, 11, 2):
    print(number)


print("\nOdd numbers:")

for number in range(1, 11, 2):
    print(number)


# Reverse range

print("\nReverse numbers:")

for number in range(10, 0, -1):
    print(number)


# Multiplication table

number = int(input("\nEnter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)