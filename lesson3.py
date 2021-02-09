# 1
def division(a, b):
    """
    Возвращает частное от деления или None.

    Именованные параметры:
    a -- делимое
    b -- делитель

    """

    try:
        return int(a / b)
    except ZeroDivisionError:
        return


first_count = int(input("Введите первое число: "))
second_count = int(input("Введите второе число: "))

print(division(first_count, second_count))


# 2
def user_data(name, surname, date_of_birth, city, email, phone):
    print(f"имя - {name}; фамилия - {surname}; год рождения - {date_of_birth}; "
          f"город проживания - {city}; email - {email}; телефон - {phone}")


user_data(
    name="Вася",
    surname="Пупкин",
    date_of_birth="13.6.1666",
    city="Москва",
    email="123@mail.com",
    phone="799999999"
)


# 3
def my_func(a, b, c):
    my_list = [a, b, c]
    my_list.remove(min(my_list))
    x, y = my_list
    return x * y


print(my_func(5, 6, 3))


# 4
def my_func1(x, y):
    validate(x, y)
    return x ** y


def my_func2(x, y):
    validate(x, y)
    a = 1 / x
    b = a
    for i in range(-1, y, -1):
        b *= a
    return b


def validate(a, b):
    if x <= 0:
        raise ValueError('Первый параметр должен быть действительным положительным числом.')
    if y >= 0:
        raise ValueError('Второй параметр должен быть целым отрицательным числом.')


x = float(input("Введите действительное положительное число: "))
y = int(input("Введите целое отрицательное число: "))

print(my_func1(x, y))
print(my_func2(x, y))


# 5
def my_func(str_num, sum_num):
    list_num = str_num.split()
    sum_num += sum(map(int, list_num))
    return sum_num


sum_num = 0

while True:
    if input('Для выхода из приложения нажмите Q, для продолжения Enter: ').upper() == 'Q':
        print(sum_num)
        break
    str_num = input("Введите строку чисел, разделенных пробелом: ")
    sum_num = my_func(str_num, sum_num)
    print(sum_num)


# 6

def int_func(var):
    """
    В зависимости от типа переданного параметра
    возвращает слово/список прописной первой буквой

    возможные типы параметра:
    str
    list

    """
    if type(var) == str:
        return var.title()
    if type(var) == list:
        return list(map(lambda x: x.title(), var))


get_string = int_func(input("Введите слово: ").lower())

new_list = (input("Введите строку из слов, разделенных пробелом: ").lower()).split()
get_list = int_func(new_list)

print(get_string)
print(get_list)
