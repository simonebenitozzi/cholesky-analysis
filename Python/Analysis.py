import numpy as np
from scipy.linalg import cholesky
from scipy.io import mmread

matrix = mmread('Matrix/apache2.mtx').toarray()
print(type(matrix))
# print(matrix)
# L = cholesky(matrix, lower=True) # np.linalg.cholesky(A)
# print(L)