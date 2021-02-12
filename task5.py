from functools import reduce

my_list = [el for el in range(100, 1000) if el % 2 == 0]

sum_num = reduce(lambda x, y: x + y, my_list)

print(sum_num)
