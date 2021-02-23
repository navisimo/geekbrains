class Matrix:
    def __init__(self, args_list):
        self.mat_list = args_list

    def __str__(self):
        items_mat = ''
        for items_list in self.mat_list:
            for item in items_list:
                items_mat += "{:>10}".format(item)
            items_mat += "\n"
        return items_mat[:-1]

    def __add__(self, other):
        for i, items_list in enumerate(self.mat_list):
            for j, item in enumerate(items_list):
                self.mat_list[i][j] = item + other.mat_list[i][j]
        return self


matr_1 = Matrix([[1, 5, 9], [9, 4, -25646], [3, 6, 9]])
matr_2 = Matrix([[2, -34564, 4], [-55555, 6, 8], [1, 2, -3]])
print(matr_1)
print('_' * 45)
print(matr_2)
print('_' * 45)
print(matr_1 + matr_2)
