import sys

password = input("Type here your password: ")
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
  
  
  
  
  
import sys

password = input("Type here your password: ")
password_length: int = password.__len__()

# Checking the password length
if password_length < 8:
  print("Your password shall include at least 8 sympols")
  sys.exit(0)
  
# Checking for capital letters availability
cap_count = 0
for i in password:
  if i.isupper():
    cap_count += 1
    break
if cap_count == 0:
  print ("Your password shall include at least one capital letter")
  sys.exit(0)
  
# Checking for special symbols
symbols = ["!", "#", "$", "%", "^", "&", "*", "~"]
symb_count = 0
while_count = 0
while while_count < symbols.__len__():
  if password.find(symbols[while_count]) != -1:
    symb_count += 1
    break
  while_count += 1
if symb_count > 0 and " " not in password:
  print("Your password has been validated successfully")
elif symb_count == 0:
  print("You password shall include at least one of these symbols: !, #, $, %, ^, &, *, ~")
  sys.exit(0)
else:
  print("No gaps shall be used")
  sys.exit(0)
