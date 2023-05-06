pi = 3.14

# 1. Calculator to calculate area of the rectangle. area = length x width
print("Here you will calculate area of the rectangle")
length = int(input("Enter the length of the rectangle: "))
width = int(input("Enter the width of the rectangle: "))
result = length * width

print(f'The area of the rectange is {result}')

# 2. This algebra monster, equation to solve a3 – b3,
# formula: (a – b)(a2 + ab + b2)
print("Solve this algebra equation a3 – b3 ")
a = int(input("Enter the value for a variable: "))
b = int(input("Enter the value for b variable: "))
result2 = (a - b)*(a**2 + a*b + b**2)

print(f'The result of this equation is: {result2}')

# 3. Area of Circle π × r2
print("Get the area of the circle")
radius = float(input("What is your radius: "))
result3 = pi * (radius**2)
rounded_result3 = round(result3, 2)

print(f"The area of the circle is {rounded_result3}")

# 4. Volume of the Sphere -> attached
print("Lets get Volume of the Sphere")
radius2 = float(input("What is the radius of your Sphere: "))
result4 = (4/3) * pi * (radius2**3)
rounded_result4 = round(result4, 2)

print(f"The area of your sphare is {rounded_result4}")

# 5. This equation x2 +  y2 +  z2 – 3xyz
# formula: (x + y + z)(x2 +  y2 +  z2 – xy – yz -xz)
print("What about the last equation? I will need 3 variables")
x = int(input("Give me an X: "))
y = int(input("Give me an Y: "))
z = int(input("Give me an Z: "))
result5 = (x + y + z) * (x**2 + y**2 + z**2 - x*y - y*z - x*z)

print(f"The result of the last one would be {result5}")


