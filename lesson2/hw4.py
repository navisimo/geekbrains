phrase = input("введите строку: ")
new_list = phrase.split()
for el in new_list:
    number = new_list.index(el)
    if len(el) > 10:
        el = el[:10]
    print(f'строка №{number + 1}, слово - {el}')
