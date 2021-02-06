# 6
# вопрос в конце кода
count_pos = int(input("Какое количество позиций необходимо записать в структуру данных «Товары»: "))
i = 0
products = []

while i < count_pos:
    name = input("введите наименование товара: ")
    price = int(input("введите цену товара: "))
    count = int(input("введите количество товара: "))
    measurement_unit = input("введите единицу изменения товара: ")

    products_dict = {
        "название": name,
        "цена": price,
        "количество": count,
        "ед": measurement_unit
    }
    i += 1

    products.append((i, products_dict))

print("структура данных", products, sep='\n')

names = []
prices = []
counts = []
measurement_units = []

for el in products:
    el = el[1]

    names.append(el.get("название"))
    prices.append(el.get("цена"))
    counts.append(el.get("количество"))
    measurement_units.append(el.get("ед"))

analyse_dict = {
        "название": names,
        "цена": prices,
        "количество": counts,
        "ед": measurement_units
  }
print("аналитика данных", analyse_dict, sep='\n')

# иногда в analyse_dict при ключе 'ед' выводятся значения  'ед': [None, None, None]}
# а иногда нормально отображается. 'ед': ['шт.', 'литр']
# из-за чего?