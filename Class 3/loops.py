animals = ['Cat', 'Dog', 'Elephant', 'Cobra11', 'Mouse']
x = 9
number = 0
# Simple While loop
while number < x:
    print(number)
    number += 1

# break, continue example
while True:
    user_input = input("Enter what you want to do? q for quit, a for print stuff")

    if user_input == 'q':
        break
    elif user_input == 'a':
        a = 5+6
        if a != 10:
            continue
        else:
            print('potato')
    else:
        print("your prompt did not match anything")

# Simple for loop
for animal in animals:
    print(animal)
#
# enumerate example
for index, animal in enumerate(animals):
    print(index, animal)

# index example, enumerate alternative
for animal in animals:
    print(f"{animal} is in index {animals.index(animal)}")

# range example
# range(101): 0 - 100
# range(50, 101): 50 - 100
# range(50, 101, 5): 50-100 increasing by 5
for number in range(50, 101, 5):
    print(number)

