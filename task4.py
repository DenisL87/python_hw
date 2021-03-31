def string_processing(instructions):
  list = []
  init_no = 0
  for operation in instructions:
    if operation == 'i':
      init_no += 1
    elif operation == 'd':
      init_no -= 1
    elif operation == 's':
      init_no *= init_no
    elif operation == 'o':
      list.append(init_no)
  return list

if __name__ == "__main__":
  print(string_processing('iiisdoso'))
  
