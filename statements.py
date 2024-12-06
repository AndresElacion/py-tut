# execute some code only if a condition is True
# they allow for basic decision-making
# (if, elif, else)

age = int(input("Enter you age: "))
has_ticket = True
price = 10.00

if age >= 55:
    print("You are a senior citizen")
    print(f"The ticket price for an senior citizen is ${price * 0.75}")
elif age >= 18:
    print("You are an adult")
    print(f"The ticket price for an adult is ${price}")
else:
    print("You are a child")
    print(f"The ticket price for an child is ${price * 0.5}")

if has_ticket:
    print("You may enter, you have a ticket")
else:
    print("You need to buy a ticket")