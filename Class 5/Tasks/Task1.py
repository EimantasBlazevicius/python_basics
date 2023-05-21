# 1. Read and Display content of the file in the most readable way you can achieve: people.txt

def fill_string_with_spaces(string, length_to_have):
    if len(string) < length_to_have:
        spaces_to_add = length_to_have - len(string)
        string = string + (' ' * spaces_to_add)
    return string


people = []
with open('files/people.txt') as f:
    header = f.readline().strip().split(',')
    content = f.readlines()
    for line in content:
        person = line.strip().split(',')

        person_to_add = {}
        for index, attribute in enumerate(person):
            person_to_add[header[index]] = attribute

        people.append(person_to_add)

# print(people)

print('-------------------------------------------------------------------------------')
for each in people:
    print(f"|{fill_string_with_spaces(each['id'], 2)} | {fill_string_with_spaces(each['first_name'], 9)} |"
          f"{fill_string_with_spaces(each['last_name'], 13)} |{fill_string_with_spaces(each['email'], 34)} |"
          f"{fill_string_with_spaces(each['gender'], 9)} |")

print('-------------------------------------------------------------------------------')