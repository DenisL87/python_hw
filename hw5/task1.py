filename = input("Type filename here: ")
if '.' in filename:
    extension = filename.split('.')
else:
    raise Exception
print(f'File extension is .{extension[-1]}')