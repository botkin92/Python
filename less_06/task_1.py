import itertools
import time

class TrafficLight:
    def __init__(self):
        self.__color = ['red', 'yellow', 'green']

    def running(self):
        for clr in itertools.cycle(self.__color):
            print(clr)
            if clr == 'red':
                time.sleep(7)
            elif clr == 'yellow':
                time.sleep(2)
            else:
                time.sleep(7)


obj = TrafficLight()
print(obj.running())
