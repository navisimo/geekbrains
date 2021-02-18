class Car:

    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police

    def go(self):
        return "Автомобиль в движении."

    def stop(self):
        return "Автомобиль остановился."

    def turn(self, turn):
        if turn == 'left' or turn == 'налево':
            return "Автомобиль повернул налево."
        elif turn == 'right' or turn == 'направо':
            return "Автомобиль повернул направо."
        else:
            return "Неверное движение автомобиля.\nАвтомобиль может поворачивать только налево/left или направо/right"

    def show_speed(self):
        return f"Автомобиль движется со скоростью: {self.speed} км/ч"


class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return "Автомобиль превышает скорость. Максимальная скорость не должна превышать 60 км/ч."
        return f"Автомобиль движется со скоростью: {self.speed} км/ч"


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return "Автомобиль превышает скорость. Максимальная скорость не должна превышать 40 км/ч."
        return f"Автомобиль движется со скоростью: {self.speed} км/ч"


class SportCar(Car):
    pass


class PoliceCar(Car):
    pass


def get_car_data(obj_car, turn):
    # def get_car_data(name_class, name, color, speed, turn, is_police=False):
    #     obj_car = name_class(name, color, speed, is_police)
    # закомментированные строчки кода нерабочие.  ВОПРОС: можно ли вытащить из строки название класса?

    print(f'Марка: {obj_car.name}\nЦвет: {obj_car.color}\nСкорость: {obj_car.speed}')
    print(f'Полицейский автомобиль: {"да" if obj_car.is_police else "нет"}')
    print('_' * 20)
    print(f'{obj_car.go()}\n{obj_car.turn(turn)}\n{obj_car.stop()}\n{obj_car.show_speed()}')
    print('*' * 40)


get_car_data(TownCar('AUDI', 'black', 120), 'left')
get_car_data(WorkCar('Volvo', 'white', 45), 'направо')
get_car_data(SportCar('AUDI', 'yellow', 200), 'right')
get_car_data(PoliceCar('LADA', 'blue', 30, True), 'error')
