# Create a user class
# initialize the fields of the user: id, name, age, city, potato
# create two methods:
#    register_user( id, name, age, city, potato):
#        responsible for returning formed user data.
#        collecting the data from userInput and storing it in the users list is not included to this method
# :
# print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
#              f"destroyed {self.potato} potatoes yesterday.")
# Adjust the code so it would still work after these adjustments.

class User:
    def __init__(self, id, name='', age='', city='', potato=''):
        self.id = id
        self.name = name
        self.age= age
        self.city = city
        self.potato = potato

    def registration_form(self):
        self.name = input("What is the user name?: ")
        self.age = input("What is the user age?: ")
        self.city = input("What is the user city?: ")
        self.potato = input("What is the potatoes input?: ")

    def display_user(self):
        print(f"The participant {self.name}, aged {self.age} years old, coming from {self.city} have "
              f"destroyed {self.potato} potatoes yesterday.")


def registration():
    if len(users) > 0:
        last_user = len(users)+1
        user = User(last_user)
    else:
        user = User(1)
    user.registration_form()
    users.append(user)


def display_users():
    for user in users:
        user.display_user()


def get_users_from_file():
    users_list = []
    with open("example.txt") as f:
        headers = f.readline().strip('\n').split(" ")
        for line in f.readlines():
            user = line.strip().split(" ")
            each_user = {}
            for index, value in enumerate(user):
                each_user[headers[index]] = user[index]
            user_from_file = User(each_user['id'], each_user['name'], each_user['age'],
                                  each_user['city'], each_user['potato'])
            users_list.append(user_from_file)
    return users_list


def save_users_to_file():
    with open('example.txt', 'w') as f:
        for key in ['id', 'name', 'age', 'city', 'potato']:
            f.write(f"{key} ")
        f.write("\n")
        for user in users:
            f.write(f"{user.id} {user.name} {user.age} {user.city} {user.potato}\n")
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
