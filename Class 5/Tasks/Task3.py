# 3. Read and Display the content of it with every single character in this file shown in reverse case. Every
# lowercase letter should become Uppercase and every upper case should become lowercase: cupcake.txt

with open('files/cupcake.txt') as f:
    text = f.read()
    for char in text:
        if char.isupper():
            print(char.lower(), end='')
        else:
            print(char.upper(), end='')
