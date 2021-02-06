my_list = [7, 5, 3, 3, 2]
new_num = int(input("введите натуральное число: "))

while new_num < 1 or new_num > 9:
    print("Число введено не верно!")
    new_num = int(input("введите число от 1 до 9: "))

if new_num == 9:
    my_list.insert(0, new_num)
elif new_num == 1:
    my_list.append(new_num)
else:
    count = 0
    for el in my_list:
        if new_num > el:
            my_list.insert(count, new_num)
        elif el == new_num:
            my_list.insert(count, new_num)
        else:
            count += 1
            continue
        break
print(my_list)
