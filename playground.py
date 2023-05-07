people = []

person = {'name': 'Eimantas', 'age': 30, 'cats': ['Yoda', 'Obi']}

people.append(person)
people.append(person)
people.append(person)
people.append(person)
people.append(person)


for human in people:
    print(f"The participant {human['name']}, aged {human['age']} years old, coming from yesterday.")
