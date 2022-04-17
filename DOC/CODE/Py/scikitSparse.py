def scikit_sparse_cholesky(A: csc_matrix, b):
    """

    If A is a sparse, symmetric, positive-definite matrix, and b is a matrix
    or vector (either sparse or dense), then the following code solves the equation Ax=b

    """
    try:
        factor = cholesky(A)
        x = factor(b)
        return x
    except Exception as e:
        raise Exception(f"Failed to execute cholesky\n Error Type: {e}")
