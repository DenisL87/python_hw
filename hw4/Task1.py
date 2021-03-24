file1 = open('file1.txt', mode='r')
string_file1 = file1.read()
print(string_file1)
file2 = open('file2.txt', mode='w')
file2.write(string_file1)


file1.close()
file2.close()