import numpy as np

# 1
vector = np.arange(10, 50)

# 2
matrix_3x3 = np.arange(9).reshape(3, 3)

# 3
identity_matrix = np.eye(3)
# 4
random_3x3x3 = np.random.rand(3, 3, 3)
# 5
random_10x10 = np.random.rand(10, 10)
min_val = random_10x10.min()
max_val = random_10x10.max()

# 6
random_vector = np.random.rand(30)
mean_value = random_vector.mean()

# 7
random_5x5 = np.random.rand(5, 5)
normalized_5x5 = (random_5x5 - random_5x5.min()) / (random_5x5.max() - random_5x5.min())

# 8
matrix_5x3 = np.random.rand(5, 3)
matrix_3x2 = np.random.rand(3, 2)
matrix_product = np.dot(matrix_5x3, matrix_3x2)

# 9
matrix_A = np.random.rand(3, 3)
matrix_B = np.random.rand(3, 3)
dot_product = np.dot(matrix_A, matrix_B)

# 10
matrix_4x4 = np.random.rand(4, 4)
transpose_4x4 = matrix_4x4.T

# 11
matrix_3x3 = np.random.rand(3, 3)
determinant = np.linalg.det(matrix_3x3)

# 12
matrix_A_3x4 = np.random.rand(3, 4)
matrix_B_4x3 = np.random.rand(4, 3)
matrix_product_AB = np.dot(matrix_A_3x4, matrix_B_4x3)

# 13
matrix_3x3 = np.random.rand(3, 3)
vector_3x1 = np.random.rand(3, 1)
matrix_vector_product = np.dot(matrix_3x3, vector_3x1)

# 14
A = np.random.rand(3, 3)
b = np.random.rand(3, 1)
solution_x = np.linalg.solve(A, b)

# 15
matrix_5x5 = np.random.rand(5, 5)
row_sums = matrix_5x5.sum(axis=1)
column_sums = matrix_5x5.sum(axis=0)


