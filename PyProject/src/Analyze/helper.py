import os
import numpy as np
from scipy.sparse import linalg as splinalg
import sys
import scipy.sparse as sparse
from scipy.io import mmread
from sksparse.cholmod import cholesky
from scipy.sparse import csc_matrix
import psutil
import csv
import math
import tracemalloc

from sympy import true

from PyProject.src.resources.costants import RESOURCES_DIRECTORY


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
    try:
        return csc_matrix(mmread(filename))

    except Exception:
        raise Exception(f"Failed to read {filename}\n")


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


def relativeError(a):
    """
    Compute the Euclidean distance between two vectors
    """

    dist = np.linalg.norm(a-1)
    return dist


def startTrackMemory():
    tracemalloc.start()


def endTrackMemory():
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def convert_size(size_bytes):
    r = float(size_bytes)
    return r/(1024*1024)


def writeCSV(name, error, memory, time):

    try:
        # csv data
        data = [name, error, memory, time]

        path = os.path.join(RESOURCES_DIRECTORY, "Py.csv")
        with open(path, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the data
            writer.writerow(data)
    except Exception:
        raise Exception("WriteCSV error")
