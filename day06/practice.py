# ==========================================
# DAY 6 - LOOP PRACTICE
# ==========================================


# 1. Print numbers from 1 to 10

print("1. Numbers from 1 to 10")

for i in range(1, 11):
    print(i)


# 2. Print even numbers

print("\n2. Even numbers from 1 to 20")

for i in range(1, 21):

    if i % 2 == 0:
        print(i)


# 3. Print odd numbers

print("\n3. Odd numbers from 1 to 20")

for i in range(1, 21):

    if i % 2 != 0:
        print(i)


# 4. Multiplication table

print("\n4. Multiplication Table")

number = int(input("Enter a number: "))

for i in range(1, 11):
    print(number, "x", i, "=", number * i)


# 5. Sum from 1 to N

print("\n5. Sum of Numbers")

n = int(input("Enter N: "))

total = 0

for i in range(1, n + 1):
    total += i

print("Sum:", total)


# 6. Count numbers divisible by 5

print("\n6. Numbers Divisible by 5")

count = 0

for i in range(1, 101):

    if i % 5 == 0:
        print(i)
        count += 1

print("Total numbers:", count)


# 7. Print string characters

print("\n7. String Characters")

text = input("Enter a word: ")

for character in text:
    print(character)


# 8. Reverse a string

print("\n8. Reverse String")

text = input("Enter a word: ")

reverse = ""

for character in text:
    reverse = character + reverse

print("Original:", text)
print("Reverse:", reverse)


# 9. Factorial

print("\n9. Factorial")

number = int(input("Enter a number: "))

factorial = 1

if number < 0:
    print("Factorial is not possible for negative numbers.")

else:

    for i in range(1, number + 1):
        factorial *= i

    print("Factorial:", factorial)


# 10. Count vowels

print("\n10. Count Vowels")

text = input("Enter a word or sentence: ")

vowel_count = 0

for character in text.lower():

    if character in "aeiou":
        vowel_count += 1

print("Number of vowels:", vowel_count)