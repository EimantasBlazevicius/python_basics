year = int(input("Enter the year: "))

if year == 0:
    print("NICE! You are not even in century  category yet")
else:
    print(f"Your are in the {((year-1) // 100) + 1} century")
