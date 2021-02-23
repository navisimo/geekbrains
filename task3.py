class Cell:
    def __init__(self, number):
        self.number = int(number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self, other):
        count = self.number - other.number
        if count <= 0:
            raise ValueError("Количество ячеек не может быть меньше нуля.")
        return Cell(count)

    def __mul__(self, other):
        return Cell(self.number * other.number)

    def __floordiv__(self, other):
        # для целочисленного деления применяется метод __floordiv__ а не __truediv__ как в задании
        return Cell(self.number // other.number)

    def make_cell(self, length_cell):
        for i in range(self.number):
            if i % length_cell == 0:
                print('\n', end='')
            print('\U0001f525', end='')


cell1 = Cell(48)
cell2 = Cell(15)

print((cell1 + cell2).number)
print((cell1 - cell2).number)
print((cell1 * cell2).number)
print((cell1 // cell2).number)
cell1.make_cell(12)
