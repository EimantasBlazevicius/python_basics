# "r" - read mode (default value).
# "w" - write mode.
# "x" - creation mode. If the file already exists, the operation fails.
# "a" - appending mode.
# "b" - binary mode.
# "t" - text mode (default value).
# "+" - updating mode (read / write).

# f = open('file.txt')
#
# print(f)
# f.close()

with open('file.txt', 'r+') as f:
    print(f)

with open("file.txt", 'r+') as f:
    print(f.readline())

with open("file.txt", 'r+') as f:
    while True:
        line = f.readline()
        if line:
            print(line)
        else:
            break

with open('file.txt', 'r+') as f:
    print(f.readlines())

with open('file.txt', 'r+') as f:
    for line in f.readlines():
        print(line)
#
# with open('file.txt', 'r+') as f:
#     for line in f.readlines():
#         #IF your data is number, and always number,
#         # int will remove not needed formating from numbers
#
#         print(int(line))

with open('file.txt', 'r+') as f:
    for line in f.readlines():
        print(line.strip("\n"))
        # print(line.lstrip("0"))
        # print(line.rstrip("0"))
        # print(line.strip("\n").rstrip("0"))


