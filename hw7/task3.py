from collections import Counter

def converter(string, separator):
  punctuation = [',', '/', '.']
  new_list = string.split(separator)
  count = 0
  while count < len(new_list):
    p_count = 0
    while p_count < len(punctuation):
      if punctuation[p_count] in new_list[count]:
        new_list[count] = new_list[count].replace(punctuation[p_count], '')
      p_count += 1
    new_list[count] = new_list[count].lower()
    count += 1
  
  new_dict = Counter(new_list)
  return new_dict


my_str = input('String')
delimiter = input('delimiter')

print(converter(my_str, delimiter))
