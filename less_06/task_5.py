class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print('Отрисовка ручкой')


class Pencil(Stationery):
    def draw(self):
        print('Отрисовка карандашом')


class Handle(Stationery):
    def draw(self):
        print('Отрисовка маркером')


obj1 = Stationery('new')
obj2 = Pen('my_pen')
obj3 = Pencil('my_pencil')
obj4 = Handle('my_handle')

obj1.draw()
obj2.draw()
obj3.draw()
obj4.draw()
