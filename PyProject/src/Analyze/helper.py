import csv
import os
import platform
import tracemalloc
from platform import uname

import numpy as np
from scipy.io import mmread
from scipy.sparse import csc_matrix
from sksparse.cholmod import cholesky

from Analysis.resources.costants import RESOURCES_DIRECTORY
from PyProject.src.Analyze.constants import LANGUAGE, OPERATING_SYSTEM, ERROR, NAME, TIME, MEMORY, ROWS, COLUMNS


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

    dist = np.linalg.norm(a - 1)
    return dist


def startTrackMemory():
    tracemalloc.start()


def endTrackMemory():
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    return peak


def convert_size(size_bytes):
    r = float(size_bytes)
    return r / (1024 * 1024)


def writeCSV(**kwargs):
    try:
        # csv data
        data = [kwargs[NAME], kwargs[ROWS],
                kwargs[COLUMNS], kwargs[ERROR],
                kwargs[MEMORY], kwargs[TIME],
                kwargs[LANGUAGE], kwargs[OPERATING_SYSTEM]]

        path = os.path.join(RESOURCES_DIRECTORY, "data.csv")
        with open(path, 'a', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)

            # write the data
            writer.writerow(data)
    except Exception:
        raise Exception("WriteCSV error")


def getOperatingSystem():
    typeOS = {
        "Windows": 0,
        "Linux": 1,
        "Darwin": 2
    }

    if in_wsl():
        return typeOS['Windows']

    plt = platform.system()
    if plt in typeOS:
        return typeOS[plt]
    else:
        return "NA"


def in_wsl() -> bool:
    return 'microsoft-standard' in uname().release
