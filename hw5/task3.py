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
while f_count < len(file_text):
    file_text[f_count] = file_text[f_count].lower()
    f_count += 1
    
f_count = 0
longest = file_text[0]
while f_count < len(file_text):
    if len(file_text[f_count]) > len(longest):
        longest = file_text[f_count]
    f_count += 1

f_count = 0
words_used = [file_text[0]]
while f_count < len(file_text):
    if file_text[f_count] not in words_used:
        words_used.append(file_text[f_count])
    f_count += 1

f_count = 0
most_used = file_text[0]
most_frequent = 1
while f_count < len(file_text):
    word_count = 1
    iteration = f_count + 1
    while iteration < len(file_text):
        if file_text[f_count] == file_text[iteration]:
            word_count += 1
        iteration += 1
    if word_count > most_frequent:
        most_used = file_text[f_count]
        most_frequent = word_count
    f_count += 1

print(f'The longest word is: {longest}')
print(f'The most used word is: {most_used}')

