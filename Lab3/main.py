import numpy as np
from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix
from tools.linearEquationsSystemSolve import linear_equations_system_solve
from tools.seidel import seidel


def print_matrix(matrix):
    print(matrix.todense())


matrix_for_dauns = sparse.csr_matrix([
    [20., 0., 5., 4., 7.],
    [-7., 3., -1., 9., 9.],
    [10., 2., -4., 2, 2.],
    [2., 9., 11., 55., 5.],
    [7., 9., 6., 9., 5.]
])  # Valera kinda daun that isn't sparse matrix

a = sparse.csr_matrix([
    [1, 0, 0, 0, 0],
    [0, 2, 1, 0, 1],
    [0, 0, 9, 0, 0],
    [0, 0, 1, 3, 0],
    [0, 7, 0, 3, 2],
])

l, u, iteration_count_decomposition = lu_decomposition(a)
inverse_a, iteration_count_inversion = inverse_matrix(a)

print("A:")
print_matrix(a)

print("L:")
print_matrix(l)

print("U:")
print_matrix(u)

print("L * U:")
print_matrix(l.dot(u))


print("Iteration number")
print(iteration_count_decomposition)
print(">-----------------------------------------<")

print("Inverse A:")
print_matrix(inverse_a)

print("(Inverse A) * A:")
print_matrix(inverse_a.dot(a))

print("Iteration number")
print(iteration_count_inversion)
print(">-----------------------------------------<")

b = sparse.csr_matrix([1., 2., 3., 4., 5.])
answer, iteration_count = linear_equations_system_solve(a, b)
print("Solution of system A with B vector [1, 2, 3, 4, 5] (lu method)")
print(answer.transpose().toarray())

print("Iteration number")
print(iteration_count)
print(">-----------------------------------------<")

b = np.array([1., 2., 3., 4., 5])
answer, iteration_count = seidel(a, b, 0.000001)
print("Solution of system A with B vector [1, 2, 3, 4, 5] (Seidel method)")
print(answer)
print("Iteration number")
print(iteration_count)
print(">-----------------------------------------<")
