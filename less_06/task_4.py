class Car:
    def __init__(self, speed, color, name, police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = bool(police)

    def go(self):
        print(f'{self.name} is going')

    def stop(self):
        print(f'{self.name} is stoping!')

    def turn(self, direction):
        if direction != 'left' or 'right':
            arg = 'Invalid argument'
        else:
            arg = f'{self.name} is turning to {direction}'
        print(arg)

    def show_speed(self):
        print(f'Current speed {self.speed} km/h')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 60:
            print('speed exceeded!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('speed exceeded!')


class PoliceCar(Car):
    pass


my_car = Car(200, 'red', 'Urus', False)
my_car.go()
my_car.show_speed()

town_car = TownCar(80, 'blue', 'Ford', False)
town_car.show_speed()
