import math

print("Welcome to Calculator 2.0")

while True:
    result = 0
    number1 = float(input("Enter the number 1: "))
    action = input("Select the action to do: \n "
                   "a - Add \n"
                   "s - Subtract \n"
                   "d - Devide \n"
                   "m - Multiply \n"
                   "p - Power Of \n"
                   "r - Sqr Root \n")
    if action != 'r':
        number2 = float(input("Enter the number 2: "))
    else:
        number2 = 0

    if action == 'a':
        result = number1 + number2
    elif action == 's':
        result = number1 - number2
    elif action == 'd':
        result = number1 / number2
    elif action == 'm':
        result = number1 * number2
    elif action == 'p':
        result = pow(number1, number2)
    elif action == 'r':
        result = math.sqrt(number1)

    print(f"The result is {result}")
    print("Would you like to do anything else?: ")
    next_action = input("Y or N?")
    if next_action.upper() == "Y":
        continue
    elif next_action.upper() == "N":
        break

