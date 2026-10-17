# ==========================================
# DAY 5 - CONDITIONAL STATEMENTS
# PRACTICE PROGRAMS
# ==========================================


# 1. CHECK EVEN OR ODD

number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")
else:
    print("Odd")


# 2. CHECK POSITIVE, NEGATIVE OR ZERO

number = float(input("\nEnter a number: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")


# 3. FIND GREATER NUMBER

num1 = float(input("\nEnter first number: "))
num2 = float(input("Enter second number: "))

if num1 > num2:
    print("First number is greater.")
elif num2 > num1:
    print("Second number is greater.")
else:
    print("Both numbers are equal.")


# 4. CHECK VOTING ELIGIBILITY

age = int(input("\nEnter your age: "))

if age >= 18:
    print("Eligible to vote.")
else:
    print("Not eligible to vote.")


# 5. STUDENT PASS OR FAIL

mark = float(input("\nEnter your mark: "))

if mark >= 40:
    print("Pass")
else:
    print("Fail")


# 6. STUDENT GRADE

mark = float(input("\nEnter your mark: "))

if mark >= 90:
    print("A+")
elif mark >= 80:
    print("A")
elif mark >= 70:
    print("B")
elif mark >= 60:
    print("C")
elif mark >= 50:
    print("D")
else:
    print("Fail")


# 7. CHECK NUMBER DIVISIBLE BY 5

number = int(input("\nEnter a number: "))

if number % 5 == 0:
    print("Number is divisible by 5.")
else:
    print("Number is not divisible by 5.")


# 8. LOGIN CHECK

username = input("\nEnter username: ")
password = input("Enter password: ")

if username == "admin" and password == "1234":
    print("Login successful.")
else:
    print("Invalid username or password.")


# 9. DISCOUNT CHECK

amount = float(input("\nEnter shopping amount: "))

if amount >= 5000:
    discount = amount * 0.20
elif amount >= 3000:
    discount = amount * 0.10
elif amount >= 1000:
    discount = amount * 0.05
else:
    discount = 0

final_amount = amount - discount

print("Discount:", discount)
print("Final Amount:", final_amount)


# 10. TEMPERATURE CHECK

temperature = float(input("\nEnter temperature: "))

if temperature >= 35:
    print("Very hot")
elif temperature >= 25:
    print("Warm")
elif temperature >= 15:
    print("Cool")
else:
    print("Cold")