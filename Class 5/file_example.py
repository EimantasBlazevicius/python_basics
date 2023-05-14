users_list = []
with open("example.txt") as f:
    headers = f.readline().strip('\n').split(" ")
    print(headers)
    for line in f.readlines():
        user = line.strip().split(" ")
        each_user = {}
        print(user)

        for index, value in enumerate(user):
            each_user[headers[index]] = user[index]

        users_list.append(each_user)


with open('example1.txt', 'w') as f:
    for key in users_list[0]:
        f.write(f"{key} ")
    f.write("\n")
    for user in users_list:
        f.write(f"{user['id']} {user['name']} {user['age']} {user['city']} {user['potato']}\n")


