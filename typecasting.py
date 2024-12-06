#  The proces of converting a variable from one datatype to another
    # str(), int(), float(), bool()

name = "Andres Dev"
age = 28
gpa = 3.2
is_student = True

gpa = int(gpa)
print(type(gpa))

age = float(age)
print(type(age))

age = str(age)
print(type(age))

name = bool(name)
print(name)