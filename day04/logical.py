print("===== LOGICAL OPERATORS =====")

age = int(input("Enter your age: "))

answer = input("Do you have an ID? (yes/no): ")
has_id = answer.lower() == "yes"

print("AND:", age >= 18 and has_id)
print("OR:", age >= 18 or has_id)
print("NOT:", not has_id)