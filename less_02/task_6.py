dict_product = {'Название': input('Введите название товара: '),
                'Цена': input('Введите цену: '),
                'Количество': input('Введите количество: '),
                'Единица_измерения': input('Введите единицу измерения: ')}
tuple_product = [(1, dict_product)]
stop_word = 'end'

for ind, el in enumerate(tuple_product, 2):
    if input('Для продолжения нажмите Enter. Чтобы закончить набор, введите "end": ') == stop_word:
        break
    tuple_product.append((ind, {'Название': input('Введите название товара: '),
                'Цена': input('Введите цену: '),
                'Количество': input('Введите количество: '),
                'Единица_измерения': input('Введите единицу измерения: ')}))
print(tuple_product)
