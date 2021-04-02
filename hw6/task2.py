def is_even(integer):
	if integer and integer % 2 == 0:
	  return True
	return False

if __name__ == "__main__":
  try:
    print(is_even(int(input('Type here: '))))
  except:
    print('Invalid value')
