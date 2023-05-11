users = []
print("Hello what would you like to do?")

while True:
    primary_action = input("1. Register new user \n"
                           "2. Display users \n"
                           "3. for close the program\n"
                           "Your choice: ")

    if primary_action == '1':
        user_name = input("What is the user name?: ")
        user_age = input("What is the user age?: ")
        user_city = input("What is the user city?: ")
        user_potatoes = input("What is the potatoes input?: ")
        users.append({'name': user_name, 'age': user_age, 'city': user_city, 'potato': user_potatoes})
    elif primary_action == '2':
        for user in users:
            print(f"The participant {user['name']}, aged {user['age']} years old, coming from {user['city']} have "
                  f"destroyed {user['potato']} potatoes yesterday.", end='\n\n')
    elif primary_action == '3':
        break
    else:
        print("Something does not seem to add up.. please read the menu options :) ")
