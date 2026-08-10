# ==========================================
# Day 3 - Type Conversion
# ==========================================

print("=" * 40)
print("       TYPE CONVERSION")
print("=" * 40)

# String to Integer
age = input("Enter your age: ")
age = int(age)

print("\nAge:", age)
print("Data Type:", type(age))

# String to Float
price = input("\nEnter product price: ")
price = float(price)

print("Price:", price)
print("Data Type:", type(price))

# Integer to String
number = 100
text = str(number)

print("\nNumber:", number)
print("Converted Value:", text)
print("Data Type:", type(text))

print("=" * 40)