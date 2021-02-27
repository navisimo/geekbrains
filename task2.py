class MyException(Exception):
    def __init__(self, txt):
        self.txt = txt


def div_func(a, b):
    try:
        a = int(a)
        b = int(b)
        if b == 0:
            raise MyException("На ноль делить нельзя")
        res = a / b
    except ValueError:
        print("Вы ввели не число")
    except MyException as err:
        print(err)
    else:
        print(res)


div_func(input("Введите длимое: "), input("Введите делитель: "))
