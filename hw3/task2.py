try:
    import random
    # ImportError
    import sdtha

    # ZeroDivisionError
    int_one = 20
    int_two = 0
    int_three = int_one / int_two

    # KeyError
    dict = {'a': 8, 'b': 0, 'c': 9, 'd': None}
    print(dict[5])

    # UnicodeError
    string = '你好'
    string = string.encode('ascii')

    # StopIteration
    for value in dict['d']:
        pass
    raise random.choice([ZeroDivisionError, ImportError, KeyError, UnicodeError, StopIteration])
except Exception as random:
    print(f"{random} error")
print('finish')
