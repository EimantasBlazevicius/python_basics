certain_text = "People Factor"

# Length of the string
print("Length of 'People Factor' is", len(certain_text))
# What is the index of the letter
print("Position of the letter in l in it is", certain_text.index('l'))
# The number of occurrences
print("The amount of times the letter p shows up is", certain_text.count('p'))
# Pick the value by index
print("At the index 7 there is a character", certain_text[7])
# Pick a range of values by index
print("In the given range [7:13] we have the characters", certain_text[7:13])
# Working with step of the list
print("Step over string by 3", certain_text[7:13:3])
reversed_variable = certain_text[7:13]
print("reverse a certain range of the list", reversed_variable[::-1])
# Lower Upper case
print("Lower case and Upper case versions:")
print(certain_text.lower())
print(certain_text.upper())

