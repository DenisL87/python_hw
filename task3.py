def converter(string, separator):
  punctuation = [',', '/', '.']
  new_list = string.split(separator)
  count = 0
  while count < len(new_list):
    p_count = 0
    while p_count < len(punctuation):
      if punctuation[p_count] in new_list[count]:
        new_list[count] = new_list[count].replace(punctuation[p_count], '')
        if new_list[count] == None:
          new_list.pop(new_list[count])
      p_count += 1
    count += 1
  
  
  pass


my_str = input()
delimiter = input()

if __name__ == "__main__":
  print(converter(my_str, delimiter))
