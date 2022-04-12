import numpy as np
from scipy.sparse import linalg as splinalg
import sys
import scipy.sparse as sparse
from scipy.io import mmread
from sksparse.cholmod import cholesky
from scipy.sparse import csc_matrix
import psutil


def getB(matrix):
    """ 
        xe = [1, 1, 1, 1, 1, 1, 1, 1, 1...]
        b = A*xe
    """
    return matrix.sum(1)  # axis 0 = column, axis 1 = row


def readMatrix(filename):
    """ 
        Read sparse matrix in csc format.
    """
    return csc_matrix(mmread(f'Matrix/{filename}.mtx'))


def scikit_sparse_cholesky(A: csc_matrix, b):
    """ 

    If A is a sparse, symmetric, positive-definite matrix, and b is a matrix 
    or vector (either sparse or dense), then the following code solves the equation Ax=b

    """

    factor = cholesky(A)
    x = factor(b)
    return x


def manual_sparse_cholesky(A):
    """ 
    The input matrix A must be a sparse symmetric positive-definite.
    Scipy does not currently provide a routine for cholesky decomposition of a sparse matrix, 
    and one have to rely on another external package such as scikit.sparse for the purpose.
    Here I implement cholesky decomposition of a sparse matrix only using scipy functions. 
    Our implementation relies on sparse LU deconposition.
    The following function receives a sparse symmetric positive-definite matrix A 
    and returns a spase lower triangular matrix L such that A = LL^T.

    """

    n = A.shape[0]
    LU = splinalg.splu(A, diag_pivot_thresh=0)  # sparse LU decomposition

    # check the matrix A is positive definite.
    if (LU.perm_r == np.arange(n)).all() and (LU.U.diagonal() > 0).all():
        return LU.L.dot(sparse.diags(LU.U.diagonal()**0.5))
    else:
        sys.exit('The matrix is not positive definite')


def relativeError(a):
    """ 
    Compute the Euclidean distance between two vectors
    """
    
    dist = np.linalg.norm(a-1)
    return dist
   

def computeMemoryUsage():
    # gives an object with many fields
    return psutil.virtual_memory().used
    

def runtimeMemoryUsage():
    # you can have the percentage of used RAM
    psutil.virtual_memory().percent
    
    
def computeCPUUsage():
    # gives a single float value
    psutil.cpu_percent()
    