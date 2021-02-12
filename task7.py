def fact(n):
    factorial = 1
    for el in range(2, n + 1):
        factorial *= el
    yield factorial


for el in fact(int(input('Получить факториал от числа: '))):
    print(el)
