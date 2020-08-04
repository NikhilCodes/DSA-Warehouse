def display_matrix(arr_2d):
    for row in arr_2d:
        print(' '.join(map(str, row)))


def zero_matrix(shape):
    row = [0 for _ in range(shape[0])]
    return [list(row) for _ in range(shape[1])]


def matrix_multiply(mat1, mat2):
    size1 = (len(mat1), len(mat1[0]))
    size2 = (len(mat2), len(mat2[0]))

    if size1[1] != size2[0]:
        raise Exception("Matrix not compatible.")

    res_matrix_size = (size1[0], size2[1])
    res_matrix = zero_matrix(res_matrix_size)
    for i in range(res_matrix_size[0]):
        for j in range(res_matrix_size[1]):
            for k in range(size1[1]):
                res_matrix[i][j] += mat1[i][k] * mat2[k][j]

    return res_matrix


if __name__ == '__main__':
    a = [
        [1, 2, 3],
        [0, 1, 2]
    ]

    b = [
        [1, 0],
        [2, 3],
        [0, 3]
    ]

    result = matrix_multiply(a, b)
    display_matrix(result)
