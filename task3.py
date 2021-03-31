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
  print(is_prime(int(input("Type here: "))))
#   number = int(input("Type here: "))
#   print(is_prime(number))
  
