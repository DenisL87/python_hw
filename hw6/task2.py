def is_even(integer):
    return bool(integer % 2 == 0)

if __name__ == "__main__":
  try:
    print(is_even(int(input('Type here: '))))
  except:
    print('Invalid value')
