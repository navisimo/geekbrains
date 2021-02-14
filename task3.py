from statistics import mean

surname_min_salary = []
sal = []

try:
    for line in open("task_3.txt", encoding='utf-8'):
        surname, salary = line.split(' ')
        salary = float(salary.replace('\n', ""))
        sal.append(salary)

        if salary < 20000:
            surname_min_salary.append(surname)
except IOError:
    print("Файла не существует!")

print(f'оклад меньше 20 тыс. руб. получают:\n{", ".join(surname_min_salary)}')
print('*' * 30)
print(f'среднее значение по окладу: {mean(sal)}')
