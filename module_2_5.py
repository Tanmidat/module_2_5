def get_matrix(n, m, value):
    matrix = []
    for i in range(n):
        matrix.append([])
        for j in range(m):
            matrix[i].append(value)
    return matrix

n = int(input('Set the number of rows of the matrix:'))
m = int(input('Set the number of columns of the matrix:'))
value = input('Set the values of the matrix: ')

matrix = get_matrix(n, m, value)

if n <= 0:
    print("The matrix is empty, the number of rows is incorrect:", n)
elif m <=0:
    print("The matrix is empty, the wrong number of columns is set:" ,m)
else:
    print("The matrix created according to your requests:")
    for i in matrix:
        print(*i)