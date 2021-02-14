count_line = 0

try:
    for line in open("task_2.txt"):
        count_line += 1
        print(f'В строке {count_line} содержится {len(line.split())} слова')
except IOError:
    print("Файла не существует!")

print('*' * 30)
print(f'всего строк в файле: {count_line}')
