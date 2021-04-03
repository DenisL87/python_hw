import json

def edit_file(file_name):
    with open(file_name) as file:
        data = json.load(file)

    for idx, q in enumerate(data.get('questions', [])):
        data['questions'][idx]['answer'] = input(q['q'])

    with open(file_name, 'w') as file:
        json.dump(data, file, indent=4)


if __name__ == '__main__':
    edit_file("questions.json")
    
