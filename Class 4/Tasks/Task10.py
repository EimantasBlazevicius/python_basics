# Task 10: Write a program to given the time of day would return a word
# Morning, Day, Evening or Night
# hint: use datetime library.
# to get current time you will need to
# from datetime import datetime
#
# current_time = datetime.now().time()

from datetime import datetime

current_time = datetime.now().time().hour


if 4 <= current_time < 12:
    print("Morning")
elif 12 <= current_time < 18:
    print("Day")
elif 18 <= current_time < 22:
    print("Evening")
elif 22 <= current_time < 24 and 0 <= current_time < 4:
    print("Night")

