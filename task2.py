import sys

password = input("type here your password: ")
password_length: int = password.__len__()
# Checking the password length
if password_length < 8:
  print("Your password shall include at least 8 sympols")
  sys.exit(0)
  
# Checking for capital letters availability
count = 0
for i in password:
  if i.isupper():
    count += 1
    break
if count == 0:
  print ("Your password shall include at least one capital letter")
  sys.exit(0)
  
# Checking for special symbols
if (password.find("$") != -1 or password.find("%") != -1 or password.find("_") != -1) and password.find(" ") == -1:
  print("Your password has been validated successfully")
else:
  if password.find("$") == -1 and password.find("%") == -1 and password.find("_") == -1:
    print("You password shall include at least one of these symbols: $, %, _")
  else:
    print("No gaps shall be used")
  sys.exit(0)
