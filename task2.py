string = input("type here your password: ")
string_length: int = string.__len__()
# Checking the password length
if string_length < 8:
  print("error")
else:
  print("correct")
# Checking for capital letters availability
count = 0
for i in string:
  if i.isupper():
    count += 1
    break
if count == 0:
  print ("error")
else:
  print("correct")
# Checking for special sympols availability
index_1 = string.find("$")
index_2 = string.find("%")
if index_2 != -1 & index_1 != -1:
  print("well done")
else:
  print("invalid")
