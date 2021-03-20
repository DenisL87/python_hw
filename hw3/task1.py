import math
import sys

first_value: str = input('Input first value: ')
if not first_value.isdigit():
    print(f'Value of type {type(first_value)} {first_value} is not a digit')
    sys.exit(0)
first_value: int = int(first_value)
operation: str = input('Input math operation: ')
if operation == '**':
    print(first_value ** 2)
    sys.exit(0)
second_value: str = input('Input second value: ')
if not second_value.isdigit():
    print(f'Value of type {type(second_value)} {second_value} is not a digit')
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
        print(first_value / second_value)
    except ZeroDivisionError:
        print("DIVISION BY ZERO!")
        sys.exit(0)
elif operation == '//':
    try:
        print(math.floor(first_value / second_value))
    except ZeroDivisionError:
        print("DIVISION BY ZERO!")
        sys.exit(0)
else:
     print(f'Invalid operation {operation}')