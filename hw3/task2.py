import random
try:
    int_one = int(input("Enter the first number "))
    int_two = int(input("Enter the second number "))
    if int_two == 0:
        raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
except:
    print(random)
print('finish')