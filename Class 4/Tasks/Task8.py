# Task 8: Write a Python program to calculate a dog's age in dog years. Note: For the first two years, a dog year is
# equal to 10.5 human years. After that, each dog year equals 4 human years. Expected Output: Input a dog's age in
# human years: 15 The dog's age in dog's years is 73

def human_to_dog_years(human_years):
    dog_years = 0
    for year in range(1, human_years+1):
        if year < 3:
            dog_years += 10.5
        else:
            dog_years += 4
    return dog_years


print(human_to_dog_years(12))
