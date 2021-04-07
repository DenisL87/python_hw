with open ('file1.txt') as file1:
    string_file1 = file1.read()
print(string_file1)

with open('file2.txt','w') as file2:
    file2.write(string_file1)

string_file1 = string_file1.swapcase()
with open('file1.txt', 'a') as file1:
    file1.write(' / ' + string_file1)
