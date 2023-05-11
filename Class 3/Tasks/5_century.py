year = int(input("Enter the year: "))

if year == 0:
    print("NICE! You are not even in century  category yet")
elif year <= 100:
    print(f"You are in the 1 century")
else:
    print(f"Your are in the {(year-1) // 100} century")
