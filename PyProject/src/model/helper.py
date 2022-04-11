import numpy as np
from scipy.sparse import linalg as splinalg
import sys
import scipy.sparse as sparse
from scipy.io import mmread
from sksparse.cholmod import cholesky
from scipy.sparse import csc_matrix



def readMatrix(filename):
    return csc_matrix(mmread(f'Matrix/{filename}.mtx'))



def scikit_sparse_cholesky(A):
    factor = cholesky(A)
    return factor
    

# The input matrix A must be a sparse symmetric positive-definite.
def manual_sparse_cholesky(A):
    """ 
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
