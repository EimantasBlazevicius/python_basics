# Tuples
magic_list = ("dog", "cat", 2000, 5.0, True)
# read methods
print(magic_list.count("dog"))
print(magic_list.index('cat'))
print(magic_list[2])

# Set

set_variable = set()
set_variable2 = {"dog", "cat", "elephant"}
# Add a new item, same as append in the list
set_variable2.add("mouse")

# Add several items at once, same as extend in the list
set_variable2.update(["bird", "horse"])

# Add the same item again
set_variable2.add("mouse")
print(set_variable2)

# Remove an item, Python will throw an error if it is not in the set, just removes value
set_variable2.remove("cat")
print(set_variable2)

# Remove an item, Python will NOT throw an error if it is not in the set, just removes value
set_variable2.discard("cat")

# Example of using set
quick_list = [1,1,1,1,1,2,2,3,6,5,4,8]
set_test = set(quick_list)
print(set_test)


# list_var = []
# dictionary_var = {'key': 'value'}
# tuple_var = ()
# set_var = {'value', 'value', 'value'}