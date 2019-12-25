class Matrix:

    def to_str(self, my_list):
        return '\n'.join([' '.join(list(map(str, el))) for el in my_list])

    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        return self.to_str(self.matrix)

    def __add__(self, other):
        all_list = []
        for i, m_list in enumerate(self.matrix):
            row = []
            for j, el in enumerate(m_list):
                row.append(el + other.matrix[i][j])
            all_list.append(row)
        return self.to_str(all_list)

matr_1 = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
matr_2 = Matrix([[6, 7, 2], [9, 8, 5], [9, 8, 7]])
print(matr_1)
print('----------')
print(matr_2)
print('----------')
print(matr_1 + matr_2)
