import sys
# _____________EMAIL VALIDATION______________
email: str = input('Input email')

try:
    if '@' not in email or '.' not in email:
        raise ValueError("add @ and . symbols")
except ValueError as error:
    print(error)
    sys.exit(0)

at_sign_index = email.index('@')
for sign in {'.', '@'}:
    try:
        if email[at_sign_index + 1] == sign or email[at_sign_index - 1] == sign:
            raise Exception('Invalid')
        elif email[-1] == sign or email[0] == sign:
            raise Exception('Invalid')
    except Exception as error:
        print(error)
        sys.exit(0)

#_____________PASSWORD VALIDATION_____________

password = input("Type here your password: ")

# Checking the password length
try:
    if len(password) < 8:
        raise ValueError("Your password shall include at least 8 symbols")
except ValueError as error:
    print(error)
    sys.exit(0)

# Checking for capital letters availability
iscapital = False
islower = False
try:
    for cap in password:
        for low in password:
            if low.islower():
                islower = True
                break
        if cap.isupper():
            iscapital = True
            break
    if not iscapital or not islower:
        raise ValueError("Your password shall consist both uppercase and lowercase letters")
except ValueError as error:
    print(error)
    sys.exit(0)

# Checking for digits
isdigit = False
try:
    for i in password:
        if i.isdigit():
            isdigit = True
            break
    if not isdigit:
        raise ValueError("Your password shall include at least one digit")
except ValueError as error:
    print(error)
    sys.exit(0)

# Checking for special symbols
symbols = ["!", "#", "$", "%", "^", "&", "*", "~"]
count = 0
while count < len(symbols):
    if symbols[count] in password:
        break
    count += 1
    try:
        if count == len(symbols):
            raise Exception("You password shall include at least one of these symbols: !, #, $, %, ^, &, *, ~")
    except Exception as error:
        print(error)
        sys.exit(0)

# Checking for gaps
try:
    if " " in password:
        raise ValueError('No gaps shall be used')
except ValueError as error:
    print(error)
    sys.exit(0)

print("Your password has been validated successfully")