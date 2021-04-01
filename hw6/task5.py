import json
def open_file(file_name):
    with open(file_name) as file:
        data = json.load(file)
    return data

def edit_file(file_name):
    with open(file_name, 'w') as file:
        file.write(json.dumps('Hello'))
    return True

if __name__ == '__main__':
    print(open_file("questions.json"))
    
    
    
# def edit_file(dict):
#   count = 0
#   while count < len(dict):
#     print(dict[count]['q'])
#     string = input('Type here: ')
#     dict[count]['a'] = string
#     count += 1
#   return dict
  
# if __name__ == "__main__":
#   dict = [{'q': 'What is your name?', 'a': ''}, {'q': 'What is your age?', 'a': ''}]
#   edit_file(dict)





# def edit_file(dict):
#   count = 0
#   while count < len(dict):
#     print(dict[count]['q'])
#     string = input('Type here: ')
#     dict[count]['a'] = string
#     print(dict[count]['a'])
#     count += 1
#   return dict
  
# if __name__ == "__main__":
#   dict = [{'q': 'What is your name?', 'a': ''}, {'q': 'What is your age?', 'a': ''}]
#   edit_file(dict)
#   print("Game over")
