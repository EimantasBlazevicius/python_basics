cars=["VW", "Audi", "BMW"]
cars.append("Zap")
cars.append("Seat")
cars.append("Cupra")
cars.extend(["Kia", "Toyota", "Mazda", "Zap", "BMW"])
print(f"Length of the list {cars}: {len(cars)}")
# Sorts the list but returns nothing, just changes the list it operates on
cars.sort()
# Creates new list that is sorted
# sorted_cars = sorted(cars)
print(f"Current state of cars list: {cars}")
# .count(x) - Amount of X occurrences in the list
print("Count", cars.count('Zap'))
# .index(x) - finds the index of the X in the list
print("Index", cars.index('Mazda'))
# .insert(index, x) - inserts the X in the index of the list
cars.insert(5, 'Toyota')
print('Insert at index', cars)
# .pop(index) - Removes the index item from the list and returns the removed value
cars.pop(5)
print("with popped value", cars)
# .pop() - Removes the last item form the list and returns it
popped_value = cars.pop()
print("with simple pop", cars, popped_value)
# .remove(x) - Removes first occurrence of the item matching the X
cars.remove("BMW")
print("removed first occurrence of BMW", cars)
# .reverse() - Reverses the order of the list
cars.reverse()
print("Reversed order", cars)
# .clear() - Clears the list entirely
cars.clear()
print("Cleared list", cars)
