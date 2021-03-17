import sys

password = input("Type here your password: ")
password_length: int = password.__len__()

# Checking the password length
if password_length < 8:
  print("Your password shall include at least 8 symbols")
  sys.exit(0)
  
# Checking for capital letters availability
caps_count = 0
for i in password:
  if i.isupper():
    caps_count += 1
    break
if caps_count == 0:
  print ("Your password shall include at least one capital letter")
  sys.exit(0)
  
# Checking for special symbols
symbols = ["!", "#", "$", "%", "^", "&", "*", "~"]
count = 0
while count < symbols.__len__():
  if symbols[count] in password:
    break
  count += 1
  if count == symbols.__len__():
    print("You password shall include at least one of these symbols: !, #, $, %, ^, &, *, ~")
    sys.exit(0)
    
# Checking for gaps
if " " in password:
  print("No gaps shall be used")
  sys.exit(0)
else:
  print("Your password has been validated successfully")
