from time import sleep


class TrafficLight:
    __color = ['red', 'yellow', 'green']

    def running(self):
        for i in range(0, 3):
            print(self.__color[i])
            sleep(7 if i == 0 else (2 if i == 1 else 5))


tl = TrafficLight()
tl.running()
