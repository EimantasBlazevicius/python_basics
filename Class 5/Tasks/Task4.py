# 4. Find the shortest word in the file and display it in the output together with the length of this word. cupcake.txt

shortest = ''
length = 99
with open('files/cupcake.txt') as f:
    words = f.read().strip().split(' ')
    for word in words:
        if len(word) < length:
            length = len(word)
            shortest = word

print(f"The shortest word with only {length} character(s) is {shortest}")
