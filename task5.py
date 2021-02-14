from random import randint

# 1 вариант
my_tuple_int = tuple(randint(13, 667) for _ in range(20))

with open('task_5.txt', 'w') as f:
    f.write(' '.join(list(map(str, my_tuple_int))))

print(sum(my_tuple_int))


# 2 вариант
my_tuple = tuple(map(str, (randint(13, 667) for _ in range(20))))

with open('task_5.txt', 'w') as f:
    f.write(' '.join(my_tuple))

with open('task_5.txt') as f:
    print(sum(list(map(int, (f.read().split(' '))))))
