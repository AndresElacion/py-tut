# used to repeat a block of code as long as a condition remains "True"
# re-check the condition at the end of the loop

""" while 1 == 1:
    #This will result to infinite loop
    print("I am stuck in a loop") """

name = input("Enter yout name: ")

while name == "":
    name = input("Enter yout name: ")

age = int(input("Enter you age: "))

while age < 0:
    print("Age cant be less then 0")
    age = int(input("Enter you age: "))
    
print(f"Hello {name}, You are {age} years old")