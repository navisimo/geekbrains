phrase = input("введите строку: ")
new_list = phrase.split()
count = 1
for el in new_list:
    if len(el) > 10:
        el = el[:10]
    print(f'строка №{count}, слово - {el}')
    count += 1
