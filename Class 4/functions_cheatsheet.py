# print("Someting")
# print(sum([5, 2]))
# listX = [1.12,5,5,6,51,3,1]
# enumerate(listX)

def hello():
    print("Hello World!")
    print("Hello World!")
    print("Hello World!")
    print("Hello World!")


hello()


def hello_with_argument(name):
    print(f"Hello {name}")


hello_with_argument("Eimantas")


def hello_with_argument_and_default_value(name="DefaultValueToMakeVariableOptional"):
    print(f"Hello {name}")


hello_with_argument_and_default_value("Gintare")
hello_with_argument_and_default_value()


def multiple_arguments(name, surname):
    print(f"{name} {surname}")


multiple_arguments("Eimantas", "Blazevicius")


def multiple_arguments_with_default_value(name, surname="Blazevicius"):
    print(f"{name} {surname}")


multiple_arguments_with_default_value("Eimantas", "Mocksurname")
multiple_arguments_with_default_value("Eimantas")
multiple_arguments_with_default_value("Mantas")


def multiple_arguments_named_values_assignment(num1, num2, num3, num4):
    print(f"{num1 + num2 + num3 + num4}")


multiple_arguments_named_values_assignment(1, 2, 3, 4)
multiple_arguments_named_values_assignment(num1=1, num3=9, num4=8, num2=1)
multiple_arguments_named_values_assignment(1, 2, num4=8, num3=3)
print("Some random text", end="159 \n\n")


def total_args(*args):
    print(args)
    for text in args:
        print(text.upper())


total_args("text1", "text1", "text1")


def total_args_with_optional_arg(*args, end="\n"):
    for text in args:
        print(text, end=end)


total_args_with_optional_arg("One", "Two", "Three", end="Some Text")


# arguments order(required, *args, optional)
def total_args_with_required_and_optional_arg(start, *args, end="\n"):
    for text in args:
        print(f"{start} - {text}", end=end)


total_args_with_required_and_optional_arg("Start", "Test", "Test", "Test", "Test", "Test")
total_args_with_required_and_optional_arg("Start", "Test", "Test", "Test", "Test", "Test", end=" End \n")


def total_kwargs(**kwargs):
    result=0
    for key in kwargs:
        result += kwargs[key]
    print(result)


total_kwargs(eggs=5, cheese=2, bread=3)


def total_kwargs_with_optional_arg(potato=5, **kwargs):
    result=0
    for key in kwargs:
        result += kwargs[key]
    print(result, end=f"  {potato} \n")


total_kwargs_with_optional_arg(wings=3, carrots=3)
total_kwargs_with_optional_arg(potato="potato", wings=3, carrots=3)
total_kwargs_with_optional_arg(wings=3, potato="potato", carrots=3)


def total_kwargs_with_required_and_optional_arg(arg1, potato=5, **kwargs):
    result = 0
    for key in kwargs:
        result += kwargs[key]
    print(f"{arg1}: {result}", end=f"  {potato} \n")


total_kwargs_with_required_and_optional_arg("The result is", 9, wings=3, carrots=3)
total_kwargs_with_required_and_optional_arg(arg1="The result is", potato=9, wings=3, carrots=3)
total_kwargs_with_required_and_optional_arg(wings=3, potato=9, carrots=3, arg1="The result is")


def total_args_and_kwargs(*args, **kwargs):
    result = 0
    for number in args:
        result += number
    for key in kwargs:
        result += kwargs[key]

    print(result)


total_args_and_kwargs(1,2,3,4,5,6, eggs=8, bacon=7)


def total_args_and_kwargs_with_optional_arg(potato, *args, **kwargs):
    result = 0
    for number in args:
        result += number
    for key in kwargs:
        result += kwargs[key]

    print(potato, result)


total_args_and_kwargs_with_optional_arg(9, 2, 3, 4, 5, 6, eggs=8, bacon=7)

# ----------------------- return version ----------------------------


def hello_return():
    return "Hello world"


print(hello_return())


def add(a, b):
    return a+b


print(add(1, 2))
print(add(1, 2)*9)

total_args_and_kwargs(add(1, 2))

# ------------------------ sum function -----------------------------


def sum1(items):
    result = 0
    for item in items:
        result += item
    return result


print(sum1([1,2,3,4,5,6,7,8,9,5,1,525,15,451,61,5461,561,651,61,6515,6]))
