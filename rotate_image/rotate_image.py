def rotate_image(matrix):

    n = len(matrix)

    if n != len(matrix[0]):
        raise ValueError("Invalid input: matrix should be n x n")

    rotated_matrix = [[0] * n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotated_matrix[j][n - 1 - i] = matrix[i][j]

    return rotated_matrix
