dictionary = {'1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
for key in dictionary:
    print(key, dictionary[key])
for key, value in dictionary.items():
    print(f'{key=}, {value=}')

print(dictionary.items())