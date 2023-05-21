# Task 7: Write a Python program that accepts a string and calculates the number of digits and letters.
# Sample Data : Python 3.2
# Expected Output :
# Letters 6
# Digits 2

text = 'Python 3.2'

number = 0
letter = 0

for char in text:
    if char.isnumeric():
        number += 1
    else:
        letter += 1

print(f"Numbers: {number} and letters: {letter}")

