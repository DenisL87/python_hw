import math
import sys
import random

try:
    first_value: str = input('Input first value: ')
    first_value: int = int(first_value)

    valid_operation = ['+', '-', '*', '/', '**', '//']
    operation: str = input('Input math operation: ')
    if operation not in valid_operation:
        raise ValueError(f'Oparation {operation} is invalid')

    if operation == '**':
        print(first_value ** 2)
        sys.exit(0)

    second_value: str = input('Input second value: ')
    second_value: int = int(second_value)

    if operation == '+':
        print(first_value + second_value)
        sys.exit(0)
    elif operation == '-':
        print(first_value - second_value)
        sys.exit(0)
    elif operation == '*':
        print(first_value * second_value)
        sys.exit(0)
    elif operation == '/':
        print(first_value / second_value)
        sys.exit(0)
    else:
        print(math.floor(first_value / second_value))
        sys.exit(0)

except (ValueError, ZeroDivisionError):
    print('error')
    raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
