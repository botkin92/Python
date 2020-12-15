import random


class LotoCard:
    def __init__(self, user_name):
        self.name = user_name
        self.card = []
        self.line_1 = []
        self.line_2 = []
        self.line_3 = []

        # Генерация карточки:
        for x in range(15):
            num = random.randint(1, 90)
            while num in self.card:
                num = random.randint(1, 90)
            self.card.append(num)

        # Сортировка по возрастанию по 5 элементов:
        self.line_1 = [self.card[i] for i in range(5)]
        self.line_2 = [self.card[i] for i in range(5, 10)]
        self.line_3 = [self.card[i] for i in range(10, 15)]
        self.line_1.sort()
        self.line_2.sort()
        self.line_3.sort()

        # Добавление пробелов в случайной позиции :
        for iter in range(4):
            self.line_1.insert(random.randint(0, 7), ' ')
            self.line_2.insert(random.randint(0, 7), ' ')
            self.line_3.insert(random.randint(0, 7), ' ')

        self.card = self.line_1 + self.line_2 + self.line_3

    def __str__(self):
        my_str_1 = ' '.join([str(elem) for elem in self.line_1])
        my_str_2 = ' '.join([str(elem) for elem in self.line_2])
        my_str_3 = ' '.join([str(elem) for elem in self.line_3])
        my_str = my_str_1 + '\n' + my_str_2 + '\n' + my_str_3
        # return f'{my_str}'
        return f'{self.name}:\n-----------------------\n' \
               f'{my_str}\n-----------------------'


human_player = LotoCard('Игрок')
computer_player = LotoCard('Компьютер')

print(human_player)
print(computer_player)
