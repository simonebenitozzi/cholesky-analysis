from posixpath import dirname
import sys

sys.path.append(dirname(__file__))

from PyProject.src.model.helper import readMatrix, scikit_sparse_cholesky




matrix = readMatrix("apache2")
print(f"\n Matrix Type: {type(matrix)} \n")
print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")
L = scikit_sparse_cholesky(matrix)
# L = cholesky(matrix, lower=True)
# L = np.linalg.cholesky(matrix)
print(L)
