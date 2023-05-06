number = 0
number2 = 0
name = "Name"
some_text = "195 meters"
a_number_with_dot = 1.1
logical_value = True

# Arithmetic operators
print(1+1)
print(7-2)
print(2*2)
print(2**4)
print(9/3)
print(9//2.9)
print(9 % 3)

# Comparison operators
print(1==2)
print(1!=2)
print(1>2)
print(1<2)
print(1>=2)
print(1<=1)

# Assignment operators
simple = "simple"
number += 5
print(number)
number -= 3
print(number)
number *= 7
print(number)
number **= 7
print(number)
number /= 9700
print(number)

# Identity operators
print(number is not number2)
print(number is number2)

# Logical operators
print(number is number2 and number is not number)
print(number is number2 or number is not number)

# Membership operators
print('x' not in some_text)

# Combining variables
print((name+' ')*5)
print(name + number)

print('The result of this text is ' + some_text + ' conducted by '+ name)
print(f"The result of this text is {some_text} conducted by {name}")


