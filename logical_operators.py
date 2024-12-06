# evaluate multiple conditions (or, and, not)
# or = at least one condition must be true
# and = both condition must be true
# not = inverts the condition (not False, not True)

temp = 20
is_raining = True

temp2 = 15
is_sunny = False

# if temp > 35 or temp < 0 or is_raining:
#     print("The outdoor event is cancelled")
# else:
#     print("The outdoor event is still scheduled")


if temp2 >= 28 and is_sunny:
    print("It is hot outside")
    print("It is sunny")
elif temp2 <= 0 and is_sunny:
    print("It is cold outside")
    print("It is sunny")
elif 28 > temp2 > 0 and is_sunny:
    print("It is warm outside")
    print("It is sunny")
elif temp2 >= 28 and not is_sunny:
    print("It is hot outside")
    print("It is cloudy")
elif temp2 <= 0 and not is_sunny:
    print("It is cold outside")
    print("It is cloudy")
elif 28 > temp2 > 0  and not is_sunny:
    print("It is warm outside")
    print("It is cloudy")