import sys

password = input("Type here your password: ")

# Checking the password length
if password.__len__() < 8:
    print("Your password shall include at least 8 symbols")
    sys.exit(0)

# Checking for capital letters availability
iscapital = False
for i in password:
    if i.isupper():
        iscapital = True
        break
if not iscapital:
    print("Your password shall include at least one capital letter")
    sys.exit(0)

# Checking for digits
isdigit = False
for i in password:
    if i.isdigit():
        isdigit = True
        break
if not isdigit:
    print("Your password shall include at least one digit")
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