num1 = int(input("Enter the number 1: "))
num2 = int(input("Enter the number 2: "))

if num1 > num2:
    print(f"{num1} is more than {num2}")
elif num2 > num1:
    print(f"{num2} is more than {num1}")
elif num1 == num2:
    print(f"{num2} is equal to {num1}")
else:
    print(f"Something went wrong")
