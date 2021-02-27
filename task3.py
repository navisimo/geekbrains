class MyException(Exception):
    txt = ''


def check_list(number, result_list):
    try:
        if number.isdigit():
            result_list.append(int(number))
        else:
            raise MyException(f'{number} - не число.')
    except MyException as err:
        print(err)

    return result_list


res_list = []
while True:
    inp_int = input('Введите число для заполнения списка или "stop" для завершения: ')
    if inp_int.lower() == 'stop':
        break
    else:
        check_list(inp_int, res_list)

print(f'корректный список: {res_list}')
