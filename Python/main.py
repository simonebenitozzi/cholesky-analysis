from posixpath import dirname
from scipy import sparse
from scipy.io import mmread
from scipy.linalg import cholesky
import numpy as np
import sys
from sksparse.cholmod import cholesky

sys.path.append(dirname(__file__))

from Python.helper import readMatrix




matrix = readMatrix("apache2")
print(f"\n Matrix Type: {type(matrix)} \n")
print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")
# L = cholesky(matrix, lower=True)
# L = np.linalg.cholesky(matrix)
# print(L)
