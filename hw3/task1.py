import math
import sys

first_value: str = input('Input first value: ')
try:
    if not first_value.isdigit():
        raise ValueError(f'Value of type {type(first_value)} {first_value} is not a digit')
    first_value: int = int(first_value)
except ValueError as error:
    print(error)
    sys.exit(0)
first_value = int(first_value)

operation: str = input('Input math operation: ')
operations = ['+', '-', '*', '/', '**', '//']
try:
    if operation not in operations:
        raise ValueError(f'Invalid operation {operation}')
except ValueError as error:
    print(error)
    sys.exit(0)

if operation == '**':
    print(first_value ** 2)
    sys.exit(0)

second_value: str = input('Input second value: ')
try:
    if not second_value.isdigit():
        raise ValueError(f'Value of type {type(second_value)} {second_value} is not a digit')
except ValueError as error:
    print(error)
    sys.exit(0)
second_value: int = int(second_value)

if operation == '+':
    print(first_value + second_value)
elif operation == '-':
    print(first_value - second_value)
elif operation == '*':
    print(first_value * second_value)
elif operation == '/':
    try:
        if second_value == 0:
            raise ZeroDivisionError("DIVISION BY ZERO!")
        else:
            print(first_value / second_value)
    except ZeroDivisionError as error:
        print(error)
        sys.exit(0)
else:
    try:
       if second_value == 0:
           raise ZeroDivisionError("DIVISION BY ZERO!")
       else:
           print(math.floor(first_value / second_value))
    except ZeroDivisionError as error:
        print(error)
        sys.exit(0)