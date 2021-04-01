 import json

def edit_file(file_name):
    with open(file_name) as file:
        data = json.load(file)
    count = 0
    while count < len(data["questions"]):
        print(data["questions"][count]["q"])
        data["questions"][count]["answer"] = input("Type your answer: ")
        count += 1
    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)
    return file

if __name__ == '__main__':
    edit_file("questions.json")
    