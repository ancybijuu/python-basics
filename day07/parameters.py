# ==========================================
# FUNCTIONS WITH PARAMETERS
# ==========================================


def greet(name):
    print("Hello", name)


greet("Ancy")
greet("Rahul")
greet("Priya")


# Two parameters

def add(a, b):
    print("Sum:", a + b)


add(10, 20)
add(50, 30)


# Student information

def student(name, age, course):
    print("\nStudent Information")
    print("Name:", name)
    print("Age:", age)
    print("Course:", course)


student("Ancy", 22, "Python Full Stack")