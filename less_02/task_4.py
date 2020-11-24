random_word = input('Введите набор слов: ')
list_word = list(random_word.split( ))

for ind, el in enumerate(list_word, 1):
    print(ind, el[:10:])
