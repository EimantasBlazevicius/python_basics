# Task 2: Create a function in such a way that we can pass any number of arguments to this function, and the function
# should process them and display each argument’s value.

def display_more_arguments(*arguments):
    for arg in arguments:
        print(arg)


display_more_arguments(1, 2, 3, 4, 5, 6, "Text", True)
