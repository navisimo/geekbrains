class ComplexNumber:
    def __init__(self, valid_part, maginary_part):
        self.valid_part = int(valid_part)
        self.maginary_part = int(maginary_part)

    def __str__(self):
        return f'{self.valid_part}, {self.maginary_part}'

    def __add__(self, other):
        return ComplexNumber(
            self.valid_part + other.valid_part,
            self.maginary_part + other.maginary_part
        )

    def __mul__(self, other):
        # z1⋅z2 =(x1+y1i)⋅(x2+y2i)=(x1⋅x2−y1⋅y2)+(x1⋅y2+x2⋅y1)i
        return ComplexNumber(
            (self.valid_part * other.valid_part) - (self.maginary_part * other.maginary_part),
            (self.valid_part * self.maginary_part) + (other.valid_part * self.maginary_part)
        )


com1 = ComplexNumber(5, 4)
com2 = ComplexNumber(9, -1)

print(com1 + com2)
print(com1 * com2)
