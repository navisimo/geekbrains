from sys import argv

try:
    print(f'payrol = {(float(argv[1]) * float(argv[2])) + float(argv[3])}')
except IndexError:
    print('Укажите 3 параметра.')
except ValueError:
    print('Тип данных указан неверно.')
