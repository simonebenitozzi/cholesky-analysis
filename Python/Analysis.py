import numpy as np
from scipy.linalg import cholesky
from scipy.io import mmread
from scipy import sparse

matrix = sparse.csr_matrix(mmread('Matrix/apache2.mtx'))
print(f"\n Matrix Type: {type(matrix)} \n")
print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")
# L = cholesky(matrix, lower=True)
L = np.linalg.cholesky(matrix)
print(L)
