# Task 6: Write a Python program to count the number of even and odd numbers in a series of numbers

def even_odd_amount(*args):
    even = 0
    odd = 0
    for arg in args:
        if arg % 2 == 0:
            even += 1
        else:
            odd += 1
    return {'even': even, 'odd': odd}


result = even_odd_amount(1, 2, 4, 6)

print('Even', result['even'])
print('Odd', result['odd'])
