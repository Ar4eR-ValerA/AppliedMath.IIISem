from scipy import sparse
from tools.luDecomposition import lu_decomposition
from tools.inverseMatrix import inverse_matrix

n = 5
# TODO: У csr_matrix дорогое обращение по индексам, поэтому логичнее использоваться lil_matrix.
# TODO: Lil_matrix немного менее эффективный по памяти, так что нужно обсудить, что в итоге использовать.
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
