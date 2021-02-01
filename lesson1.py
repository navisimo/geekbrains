# 1
a = 1
b = 2
print(a, b)

first_num = int(input('Введите число: '))
second_num = int(input('Введите число: '))
first_str = input('Введите слово: ')
print(first_num, second_num, first_str)


# 2
seconds = int(input('Введите число (секунд): '))

minutes = seconds // 60
hours = minutes // 60

print("%02d:%02d:%02d" % (hours, minutes % 60, seconds % 60))


# 3
number = input('Введите число: ')
num_1 = int(number)
num_2 = int(number * 2)
num_3 = int(number * 3)
print(num_1 + num_2 + num_3)


# 4
number = int(input('Введите число: '))
largest_number = 0

while number // 10 != 0:
    last_digit = number % 10
    number = number // 10

    if largest_number < last_digit:
        largest_number = last_digit

if number > largest_number:
    print(f'наибольшая цифра: {number}')
else:
    print(f'наибольшая цифра: {largest_number}')


# 5
revenue = int(input('Введите выручку: '))
costs = int(input('Введите издержки: '))

if revenue < costs:
    print('издержки больше выручки')
elif revenue == costs:
    print('издержки и выручка фирмы совпадают')
else:
    profit = revenue - costs
    profitability = format(profit / revenue, '.2f')
    print(f'выручка больше издержек, рентабельность выручки фирмы составляет : {profitability}')
    people = int(input('Введите количество сотрудников: '))
    profit_per_employee = profit / people
    print(f'прибыль фирмы в расчёте на одного сотрудника составляет : {profit_per_employee}')


# 6
distance = int(input('В первый день спортсмен пробежал: '))
required_distance = int(input('Сколько километров болжен пробежать спортсмен? - '))
count = 1

print('Результат:')
print(f'1-й день: {distance}')

while distance < required_distance:
    distance = distance + distance * 0.1
    count += 1
    print('%d-й день: %.2f' % (count, distance))

print(f'Ответ: На {count}-й день спортсмен достиг результата — не менее {required_distance} км.')








