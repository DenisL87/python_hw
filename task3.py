import sys
import math

first_value: str = input('Input first value: ')
operation: str = input('Input math operation: ')
if operation == '**':
  second_value = first_value
  print(int(second_value) * int(first_value))
  sys.exit(0)
second_value: str = input('Input second value: ')

for value in {first_value, second_value}:
  if not value.isdigit():
    print(f'Value of type {type(value)} {value} is not a digit')
    sys.exit(0)
  first_value: int = int(first_value)
  second_value: int = int(second_value)
   
  if operation == '+':
    print(first_value + second_value)
  elif operation == '-':
    print(first_value - second_value)
  elif operation == '*':
    print(first_value * second_value)
  elif operation == '/':
    if second_value == 0:
      print("division by zero")
      sys.exit(0)
    else:
      print(first_value / second_value)
  elif operation == "//":
    if second_value == 0:
      print("division by zero")
      sys.exit(0)
    else:
      print(math.floor(first_value / second_value))
  else:
    print(f'Invalid operation {operation}')

    
    import sys
import math

first_value: str = input('Input first value: ')
if not first_value.isdigit():
  print(f'Value of type {type(first_value)} {first_value} is not a digit')
  sys.exit(0)
operation: str = input('Input math operation: ')

if operation == '**':
  second_value = first_value
  print(int(second_value) * int(first_value))
  sys.exit(0)
  
second_value: str = input('Input second value: ')
if not second_value.isdigit():
  print(f'Value of type {type(second_value)} {second_value} is not a digit')
  sys.exit(0)
   
if operation == '+':
  print(first_value + second_value)
elif operation == '-':
  print(first_value - second_value)
elif operation == '*':
  print(first_value * second_value)
elif operation == '/':
  if second_value == 0:
    print("division by zero")
    sys.exit(0)
  else:
    print(first_value / second_value)
elif operation == "//":
  if second_value == 0:
    print("division by zero")
    sys.exit(0)
  else:
    print(math.floor(first_value / second_value))
else:
  print(f'Invalid operation {operation}')
