import time
from itertools import cycle

class TrafficLight:

    def __init__(self):
        self.__color = None

    def running(self):
        for item in cycle([('red', 7), ('yellow', 2), ('green', 10), ('yellow', 2)]):
            self.__color = item[0]
            print(self.__color)
            time.sleep(item[1])

obj = TrafficLight()
obj.running()