class Date:
    def __init__(self, d_m_y):
        self.d_m_y = d_m_y

    @classmethod
    def get_int(cls):
        inp_date = cls(date)
        t_tuple = ('день', 'месяц', 'год')

        for i, number in enumerate(inp_date.d_m_y.split('-')):
            try:
                number = int(number)
                if inp_date.validate_date(i, number):
                    print(f'{t_tuple[i]}: {number}.')
                else:
                    print(f'{t_tuple[i]} не может быть: {number}.')
            except ValueError:
                print(f'{number} - это не число.')

    @staticmethod
    def validate_date(i, number):
        if i == 0:
            return True if 1 <= number <= 31 else False
        elif i == 1:
            return True if 1 <= number <= 12 else False
        elif i == 2:
            return True if 1970 <= number <= 2070 else False


date = '01-12-2021'
d = Date(date)
d.get_int()

date = '61-16-прпр'
d = Date(date)
d.get_int()
