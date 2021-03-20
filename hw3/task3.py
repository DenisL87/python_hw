list = []
for i in range(187):
    if i % 5 == 0 and i != 0:
        list.append(i)
print(list)

max_el = list[0]
for i in list:
    if i > max_el:
        max_el = i
print(f'Max element: {max_el}')

min_el = max_el
sum = 0
for i in list:
    sum += i
    if i < min_el and i != 0:
        min_el = i
print(f'Min element: {min_el}')
print(f'sum: {sum}')
