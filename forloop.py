# used to iterate over a sequest (string, list, tuple, set)
# repeat a block of code an exact amout of times

# import time

# for i in range(10, 0, -1):
#     print(i)
#     time.sleep(1)

# print("HAPPY NEW YEAR!")

"""  """
# List [] = mutable, most flexible
# Tuple () = immutable, faster
# Set {} = mutable (add/remore), unordered, NO duplicates, best for membership testing

""" LIST """
# fruits = ["apple", "mango", "orange"]
# fruits[0] = "pineapple"
# fruits.append("coconut")
# fruits.remove("apple")
# fruits.pop(1)
# fruits.clear()

""" TUPLE """
# fruits = ("apple", "mango", "orange")

""" SET """
fruits = {"apple", "mango", "orange"}
# fruits.add("pineapple")
# fruits.remove("apple")
# fruits.clear()

""" for fruit in fruits:
    print(fruit, end=" ") """

fruit = input("Enter a fruit to search for: ")

if fruit in fruits:
    print(f"{fruit} was found.")
else:
    print(f"{fruit} was not found")