import numpy as np
from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix
from tools.linearEquationsSystemSolve import linear_equations_system_solve
from tools.seidel import seidel

a = sparse.csr_matrix([[10., -3., 5.], [-7., 6., -1.], [0., 2., 5.]])

l, u = lu_decomposition(a)
inverse_a = inverse_matrix(a)

print("A:")
print(a)

print("L:")
print(l)

print("U:")
print(u)

print("L * U:")
print(l.dot(u))

print("Inverse A:")
print(inverse_a)

print("(Inverse A) * A:")
print(inverse_a.dot(a))

b = sparse.csr_matrix([[1.], [2.], [3.]])
print("Solution of system A with B vector [1, 2, 3] (lu method)")
print(linear_equations_system_solve(a, b).transpose().toarray())

b = np.array([1., 2., 3.])
print("Solution of system A with B vector [1, 2, 3] (Seidel method)")
print(seidel(a, b, 0.000001))
