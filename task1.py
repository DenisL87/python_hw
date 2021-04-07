arr = [5, 96, 2]
total_string = str(arr[0])
count = 1
while count < len(arr):
  total_string += str(arr[count])
  count += 1

total_number = int(total_string)
print(total_number)
