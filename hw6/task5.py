import json

def edit_file(file_name):
    answers = []
    with open(file_name) as file:
        data = json.load(file)
        count = 0
        while count < len(data["questions"]):
            print(data["questions"][count]["q"])
            answers.append(input("Type your answer: "))
            count += 1

    with open(file_name, 'w') as file:
        count = 0
        while count < len(data["questions"]):
            file["questions"][count]["answer"].write(json.dump(answers[count]))
    return file_name

if __name__ == '__main__':
    edit_file("questions.json")
    
