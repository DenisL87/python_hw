from functools import reduce

arr = [52, 9, 1, 30, 200]
max_int = reduce(lambda x, y: x + y, map(str, sorted(arr, key = str, reverse = True)))
print(max_int)
