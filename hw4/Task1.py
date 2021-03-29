file1 = open('file1.txt', mode='r')
string_file1 = file1.read()
file1.close()
print(string_file1)

file2 = open('file2.txt', mode='w')
file2.write(string_file1)
file2.close()

string_file1 = string_file1.swapcase()
file1 = open('file1.txt', mode='a')
file1.write(' / ' + string_file1)
file1.close()

# with open('file1.txt', mode='r') as file1:
#   string_file1 = file1.read()
# print(string_file1)

# with open('file2.txt', mode='w') as file2:
#   file2.write(string_file1)

# string_file1 = string_file1.swapcase()
# with open('file1.txt', mode='a') as file1:
#   file1.write(' / ' + string_file1)
