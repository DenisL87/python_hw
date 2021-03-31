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