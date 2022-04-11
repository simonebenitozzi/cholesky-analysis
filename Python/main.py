from posixpath import dirname

from scipy import sparse
from scipy.io import mmread
from scipy.linalg import cholesky
from scipy.sparse import csc_matrix
import numpy as np
import sys

sys.path.append(dirname(__file__))

from Python.helper import readMatrix, sparse_cholesky




matrix = csc_matrix(readMatrix("apache2"))
print(f"\n Matrix Type: {type(matrix)} \n")
print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")
L = scikit_sparse_cholesky(matrix)
# L = cholesky(matrix, lower=True)
# L = np.linalg.cholesky(matrix)
print(L)
