def is_even(integer):
  if integer % 2 == 0 and integer != 0:
    return True
  else:
    return False

if __name__ == "__main__":
  print(is_even(int(input('Type here: '))))
