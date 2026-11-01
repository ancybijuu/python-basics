n = int(input("Enter the number of terms: "))

a = 0
b = 1

if n <= 0:
    print("Enter a positive number")
else:
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b