# Task 3: Write a program to create function calculation() such that it can accept two variables and calculate
# addition and subtraction. Also, it must return both addition and subtraction in a single return call.
# def calculation(a, b): # Your Code
#
# res = calculation(40, 10)
# print(res)
# Expected Output:
# 50, 30

def calculation(a, b):
    return {'addition': a+b, 'subtraction': a-b}


result = calculation(15, 2)

print('Addition', result['addition'])
print('Subtraction', result['subtraction'])
