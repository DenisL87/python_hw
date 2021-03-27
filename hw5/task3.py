with open('file1.txt', 'r') as file:
    file_text = file.read().split(" ")

punctuation = ['.', ',', ';', '(', ')']
f_count = 0
while f_count < len(file_text):
    p_count = 0
    while p_count < len(punctuation):
        if punctuation[p_count] in file_text[f_count]:
            file_text[f_count] = file_text[f_count].replace(punctuation[p_count], '')
        p_count += 1
    f_count += 1

f_count = 0
longest = file_text[0]
most_used = file_text[0]
while f_count < len(file_text):
    if len(file_text[f_count]) > len(longest):
        longest = file_text[f_count]
    f_count += 1

print(f'The longest word is: {longest}')
print(f'The most used word is: {most_used}')
