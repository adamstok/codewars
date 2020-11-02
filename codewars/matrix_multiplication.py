def matrix_multiplication(matrix1, matrix2):
    n = 0
    outp = []
    for i in range(len(matrix1)):
        level = []
        for j in range(len(matrix1[i])):
            for count in range(len(matrix1[i])):
                n += matrix1[i][count] * matrix2[count][j]
            level.append(n)
            n = 0
        outp.append(level)
    return outp


m1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
m2 = [[1, 1, 1], [2, 2, 2], [3, 3, 3]]
print(matrix_multiplication(m1, m2))
