def is_prime(integer):
  count = 2
  if integer > 1:
    while count < integer:
      if integer % count == 0:
        return False
      count += 1
    return True
  else:
    return False

if __name__ == "__main__":
  try:
    print(is_prime(int(input("Type here: "))))
  except:
    print('Invalid value')
  
