with open("task_1.txt", "w", encoding='utf-8') as f_obj:
    while True:
        if input('Для выхода из приложения нажмите пробел, для продолжения Enter: ').upper() == ' ':
            break
        f_obj.write(input("Введите данные: ") + '\n')
