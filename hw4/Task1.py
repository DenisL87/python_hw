file1 = open('file1.txt', mode='r')
string_file1 = file1.read()
print(string_file1)
file2 = open('file2.txt', mode='w')
file2.write(string_file1)
file2.close()

file1 = open('file1', mode='a')
string_file1 = string_file1.swapcase()
file1.append('. ' + string_file1) # or file1.write('. ' + string_file1)
file1.close()

# file1 = open('file1.txt', mode='r+')
# new_string = file1.read().swapcase()
# file1.write(new_string)
# file1.close()
# print(new_string)

#for i in file1:
    

# for i in new_string:
#     if i.islower():
#         new_string[i].swapcase()
# file1.close()
# print(new_string)
