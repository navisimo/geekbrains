class Stationery:

    def __init__(self, title):
        self.title = title

    def draw(self):
        return "Запуск отрисовки."


class Pen(Stationery):
    def draw(self):
        return "Ручкой заполняют документы."


class Pencil(Stationery):
    def draw(self):
        return "Карандашом делают зарисовки."


class Handle(Stationery):
    def draw(self):
        return "Маркером выделяют главные моменты."


def get_stationery_data(obj):
    print(f'Название: {obj.title}\n{obj.draw()}')
    print('*' * 35)


get_stationery_data(Pen('Ручка'))
get_stationery_data(Pencil('Карандаш'))
get_stationery_data(Handle('Маркер'))
