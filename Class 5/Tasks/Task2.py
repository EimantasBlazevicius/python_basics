# 2. Read and Display content in the output, but sort the data based on votes received, Highest to Lowest:
# eurovision.txt

participants = []
with open('files/eurovision2019.txt') as f:
    header = f.readline().strip().split(',')
    content = f.readlines()
    for line in content:
        artist = line.strip().split(',')

        person_to_add = {}
        for index, attribute in enumerate(artist):
            person_to_add[header[index]] = attribute

        participants.append(person_to_add)

sorted_participants = sorted(participants, key=lambda d: int(d['Jury Votes']), reverse=True)
print(sorted_participants)
