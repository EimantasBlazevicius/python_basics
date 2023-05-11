weight = float(input("Provide the weight(kg): "))
height = float(input("Provide the height(m): "))

bmi = weight / (height * height)

if bmi <= 18.5:
    print("Underweight")
if bmi <= 25.0:
    print("Normal")
if bmi <= 30.0:
    print("Overweight")
if bmi > 30:
    print("Obese")
