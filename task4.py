import uuid


class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self):
        self.division = {
            'accounting': [],
            'purchasing_department': [],
            'sales_department': []
        }

        self.account = {
            'Printer': {
                'ids': [],
                'count': 0
            },
            'Scanner': {
                'ids': [],
                'count': 0
            },
            'Copier': {
                'ids': [],
                'count': 0
            }
        }

    @staticmethod
    def description():
        print("склад оргтехники.")

    def reception(self, obj):
        self.account[obj.__class__.__name__]['ids'].append(str(obj.id))
        self.account[obj.__class__.__name__]['count'] += 1
        print(self.account)

    def uses(self, div, obj):
        self.division[div].append(str(obj.id))
        print(self.division)


class OfficeEquipment:
    def __init__(self, name, price):
        self.id = uuid.uuid4()
        self.name = name
        self.price = price


class Printer(OfficeEquipment):
    def __init__(self, name, price, model):
        self.model = model
        super().__init__(name, price)


class Scanner(OfficeEquipment):
    def __init__(self, name, price, type_sc):
        self.type_sc = type_sc
        super().__init__(name, price)


class Copier(OfficeEquipment):
    def __init__(self, name, price, print_technology):
        self.print_technology = print_technology
        super().__init__(name, price)


w = Warehouse()
Warehouse.description()


while True:
    try:
        count = int(input(f'Сколько единиц одного вида оргтехники должен получить склад: '))
        if count <= 0:
            raise MyException("Необходимо ввести число больше 0.")
    except ValueError:
        print("Вы ввели не число.")
    except MyException as err:
        print(err)
    else:
        eq_tuple = ('Printer', 'Scanner', 'Copier')
        type_sc = ('tablet', 'lingering', 'hand', 'slide')
        print_tech = ('laser', 'light-emitting diode', 'tverdochernilny')
        model = ('matrix', 'inkjet', 'laser', 'LED')
        while True:
            equipment = input(f'Какой вид оргтехники должен получить склад? {eq_tuple}: ')
            try:
                if equipment.capitalize() in eq_tuple:
                    for i in range(count):
                        name = input(f'Введите название {i + 1}-ой оргтехники {equipment}: ')
                        while True:
                            try:
                                price = int(input(f'Введите стоимость {equipment}: '))
                                break
                            except ValueError:
                                print("Вы ввели не число.")
                        if equipment == 'Scanner':
                            while True:
                                try:
                                    value = input(f'Выберете вид из списка {type_sc}: ')
                                    type_sc.index(value)
                                    break
                                except ValueError:
                                    print("Такого вида не существует.")
                            print(Scanner(name, price, value).__dict__.values())
                        if equipment == 'Copier':
                            while True:
                                try:
                                    value = input(f'Выберете технологию печати из списка {print_tech}: ')
                                    print_tech.index(value)
                                    break
                                except ValueError:
                                    print("Такой технологии не существует")
                            print(Copier(name, price, value).__dict__.values())
                        if equipment == 'Printer':
                            while True:
                                try:
                                    value = input(f'Выберете модель из списка {model}: ')
                                    model.index(value)
                                    break
                                except ValueError:
                                    print("Такой модели не существует")
                            print(Printer(name, price, value).__dict__.values())
                    break
                else:
                    print(f"Такого вида оргтехники не существует. Выберете вид из списка - {eq_tuple}")
            except MyException as err:
                print(err)
        break


pri = Printer('printer', 300, 'matrix')
pri1 = Printer('printer', 300, 'matrix')

w.reception(pri)
w.reception(pri1)
w.uses('accounting', pri)
print(w.__dict__.values())
