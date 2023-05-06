# print versions
print("Some interesting Text")
print("From loop", 3.2)
print("at the start", 9)
print("Sugar", "Cookie", sep=" ")
print("Sugar", "Cookie", sep=" POWER ", end=". \n\n")

# formatting methods
title="Mr."
name="Eimantas"

# printf
print("Hello there, %s %s" % (title, name), end="\n\n")

# str.format()
print("Hello there, {} {}".format(title, name))
print("Hello there, {name} {title}".format(title=title, name=name))
print("Hello there, {1} {0}".format(title, name), end="\n\n")

# f-string
print(f"Hello there, {title} {name}", end="\n\n")
# Changing the way the variable is displayed
n = 109.2345654324
print(f"{n:.3f}")  # will display 109.234
print(f"{round(n,3)}")  # will display 109.234

percent = 0.71
print(f"{percent:.1%}")  # will display 71.0%


