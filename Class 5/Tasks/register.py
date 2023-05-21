def registration():
    user_name = input("What is the user name?: ")
    user_age = input("What is the user age?: ")
    user_city = input("What is the user city?: ")
    user_potatoes = input("What is the potatoes input?: ")
    last_user = users[len(users)-1]
    users.append({'id': int(last_user['id'])+1, 'name': user_name, 'age': user_age, 'city': user_city, 'potato': user_potatoes})


def display_users():
    for user in users:
        print(f"The participant {user['name']}, aged {user['age']} years old, coming from {user['city']} have "
              f"destroyed {user['potato']} potatoes yesterday.")


def get_users_from_file():
    users_list = []
    with open("../../Class 6/Tasks/example.txt") as f:
        headers = f.readline().strip('\n').split(" ")
        for line in f.readlines():
            user = line.strip().split(" ")
            each_user = {}
            for index, value in enumerate(user):
                each_user[headers[index]] = user[index]
            users_list.append(each_user)
    return users_list


def save_users_to_file():
    with open('../../Class 6/Tasks/example.txt', 'w+') as f:
        for key in users[0]:
            f.write(f"{key} ")
        f.write("\n")
        for user in users:
            f.write(f"{user['id']} {user['name']} {user['age']} {user['city']} {user['potato']}\n")
    print("Your users were saved successfully")


print("Hello what would you like to do?")
users = get_users_from_file()

while True:
    primary_action = input("1. Register new user \n"
                           "2. Display users \n"
                           "3. for close the program\n"
                           "Your choice: ")

    if primary_action == '1':
        registration()
    elif primary_action == '2':
        display_users()
    elif primary_action == '3':
        save_users_to_file()
        break
    else:
        print("Something does not seem to add up.. please read the menu options :) ")
