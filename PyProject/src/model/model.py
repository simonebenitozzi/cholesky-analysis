import time
from pathlib import Path
import sys
import os

import numpy as np

myDir = os.getcwd()
sys.path.append(myDir)

path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)


from PyProject.src.model.helper import computeMemoryUsage, readMatrix, relativeError, scikit_sparse_cholesky, getB

def main():
    matrix = readMatrix("apache2")
    b = getB(matrix)
    
    print(f"b: ---- \n {b} \n -----")
    print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")



    x = scikit_sparse_cholesky(matrix, b)
    print(type(x))
    print(f"x: ---- \n {x} \n -----")
    
    
    # compute distance 
    dist = relativeError(x)
    print(f"DISTANCE: {dist} \n")


if __name__ == '__main__':
    start_time = time.time()
    start_memory = computeMemoryUsage()
    main()
    print("--- %s memory ---" % (computeMemoryUsage() - start_memory))
    print("--- %s seconds ---" % (time.time() - start_time))
    
