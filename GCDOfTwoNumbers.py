num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

a = abs(num1)
b = abs(num2)

while b != 0:
    a, b = b, a % b

print("GCD:", a)