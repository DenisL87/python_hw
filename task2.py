string = input("type here you password: ")
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
symbol_1 = string.find("$")
symbol_2 = string.find("%")
symbol_3 = string.find("_")
if symbol_1 != -1 & symbol_2 != -1 & symbol_3 != -1:
  print("well done")
else:
  print("invalid")
