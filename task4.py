numbers = {
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four': 'Четыре'
}

try:
    for line in open("task_4.txt", encoding='utf-8'):
        number_s, number_d = line.split(' — ')
        number_s = numbers.get(number_s)
        with open("task_4_1.txt", "a", encoding='utf-8') as f:
            f.write(f'{number_s} - {number_d}')
except IOError:
    print("Файла не существует!")
