# --------------------------Write----------------------
with open('file.txt', 'a') as f:
    f.write("Some New text\n")
    f.write("Some New textasd\n")

with open('file.txt', 'a') as f:
    f.writelines(['Str1\n', 'Str2\n', 'Str3\n'])
