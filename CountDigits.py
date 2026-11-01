number = int(input("Enter a number: "))

count = 0

if number == 0:
    count = 1
else:
    number = abs(number)

    while number > 0:
        count += 1
        number = number // 10

print("Total digits:", count)