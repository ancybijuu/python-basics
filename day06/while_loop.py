# ==========================================
# DAY 6 - WHILE LOOP
# ==========================================

print("Numbers from 1 to 10:")

number = 1

while number <= 10:
    print(number)
    number += 1


print("\nEven numbers from 1 to 20:")

number = 2

while number <= 20:
    print(number)
    number += 2


print("\nCountdown:")

number = 10

while number >= 1:
    print(number)
    number -= 1

print("Blast off! 🚀")


# User controlled loop

print("\nEnter 0 to stop.")

while True:

    number = int(input("Enter a number: "))

    if number == 0:
        print("Loop stopped.")
        break

    print("You entered:", number)