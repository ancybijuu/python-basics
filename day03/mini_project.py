# ==========================================
# Day 3 Mini Project
# Student Information System
# ==========================================

print("=" * 50)
print("       STUDENT INFORMATION SYSTEM")
print("=" * 50)

# Get student information
student_name = input("Student Name: ")
roll_number = input("Roll Number: ")
department = input("Department: ")
semester = input("Semester: ")
college = input("College: ")
cgpa = float(input("CGPA: "))

# Display student information
print("\n" + "=" * 50)
print("            STUDENT REPORT")
print("=" * 50)

print(f"Student Name : {student_name}")
print(f"Roll Number  : {roll_number}")
print(f"Department   : {department}")
print(f"Semester     : {semester}")
print(f"College      : {college}")
print(f"CGPA         : {cgpa}")

print("=" * 50)
print("       INFORMATION SAVED")
print("=" * 50)