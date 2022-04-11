from scipy.sparse import linalg as splinalg
import scipy.sparse as sparse
import sys


# The input matrix A must be a sparse symmetric positive-definite.
def sparse_cholesky(A):

    n = A.shape[0]
    LU = splinalg.splu(A, diag_pivot_thresh=0)  # sparse LU decomposition

    # check the matrix A is positive definite.
    if (LU.perm_r == np.arange(n)).all() and (LU.U.diagonal() > 0).all():
        return LU.L.dot(sparse.diags(LU.U.diagonal()**0.5))
    else:
        sys.exit('The matrix is not positive definite')
