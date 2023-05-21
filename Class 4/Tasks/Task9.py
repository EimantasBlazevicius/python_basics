# Task 9: Write a Python program to convert a month name to a number of days.
# Expected Output:
# List of months: January, February, March, April, May, June, July, August
# , September, October, November, December
# Input the name of Month: February
# No. of days: 28/29 days

months_dict={'January': 31, 'February': '28/29', 'March': 31, 'April': 30, 'May': 31,
             'June': 30, 'July': 31, 'August': 31, 'September': 30, 'October': 31, 'November': 30, 'December': 31}

print("List of months: January, February, March, April, May, June, July, August, September, October, November, "
      "December")

selected_month = input('Input the name of Month: ')
if selected_month in months_dict:
    print(f"{selected_month} has {months_dict[selected_month]} days")
else:
    print("Not a month")

