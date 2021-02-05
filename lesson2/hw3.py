num = int(input("введите номер месяца: "))
while num < 1 or num > 12:
    num = int(input("ошибка, введите еще раз номер месяца (от 1 до 12): "))
# dict
my_dict = {
    "winter": (1, 2, 12),
    'spring': (3, 4, 5),
    'summer': (6, 7, 8),
    'autumn': (9, 10, 11)
}
for season in my_dict.keys():
    if num in my_dict[season]:
        print(season)

# list
my_list = ['winter', 'spring', 'summer', 'autumn']

if num in [1, 2, 12]:
    print(my_list[0])
elif num in [3, 4, 5]:
    print(my_list[1])
elif num in [6, 7, 8]:
    print(my_list[2])
elif num in [9, 10, 11]:
    print(my_list[3])
