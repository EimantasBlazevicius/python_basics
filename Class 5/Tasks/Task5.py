# 5. Find the average for all numbers in each line, then find the average of those average values and finally append
# the file with this one number in the new line: numbers.txt

average_of_each_line = []
with open('files/numbers.txt') as f:
    lines = f.readlines()
    for line in lines:
        numbers_list = line.strip().split('  ')
        total = 0
        for number in numbers_list:
            total += int(number)
        average_of_each_line.append(total/len(numbers_list))

final_average = sum(average_of_each_line) / len(average_of_each_line)
print(final_average)
