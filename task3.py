class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {'wage': int(wage), 'bonus': int(bonus)}

    @property
    def income(self):
        return self._income


class Position(Worker):

    def get_full_name(self):
        return f'{self.position}: {self.name} {self.surname}'

    def get_total_income(self):
        return f"общий доход в месяц составляет: {self._income.get('wage') + self._income.get('bonus')} руб."


def get_worker_data(name, surname, position, wage, bonus):
    p_w = Position(name, surname, position, wage, bonus)
    print(f'Имя: {p_w.name}\nФамилия: {p_w.surname}\nДолжность: {p_w.position}')
    print(f'Оклад: {p_w.income["wage"]}\nПремия: {p_w.income["bonus"]}')
    print('_' * 20)
    print('{}\n{}'.format(p_w.get_full_name(), p_w.get_total_income()))
    print('*' * 30)


get_worker_data('Игнат', 'Плюшкин', 'Начальник', 100000, 50000)
get_worker_data('Иннокентий', 'Дробовиков', 'Зам. начальника', 80000, 20000)
get_worker_data('Аркадий', 'Виноградов', 'Уборщик', 30000, 5000)
