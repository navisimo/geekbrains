from itertools import count, cycle


def generate_int(first_num, last_num):
    for el in count(first_num):
        if el > last_num:
            break
        else:
            yield el


def repeat_list_items(some_list, last_i):
    с = 0
    for el in cycle(some_list):
        if с >= last_i:
            break
        yield el
        с += 1


g_i = generate_int(3, 10)
print(g_i)

for el in g_i:
    print(el)

g_l = repeat_list_items('QWERTY', 18)
print(g_l)

for el in g_l:
    print(el)
