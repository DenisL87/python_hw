import sys

string = input("type here your password: ")
string_length: int = string.__len__()
# Checking the password length
if string_length < 8:
  print("error")
  sys.exit(0)
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
  sys.exit(0)
else:
  print("correct")
# Checking for special sympols availability
if (string.find("$") != -1 or string.find("%") != -1 or string.find("_") != -1) and string.find(" ") == -1:
  print("well done")
else:
  print("invalid")
  sys.exit(0)
