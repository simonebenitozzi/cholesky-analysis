from pathlib import Path
from posixpath import dirname

import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)

path = Path(myDir)
a = str(path.parent.absolute())

sys.path.append(a)

if __name__ == '__main__':

    import numpy as np
    from PyProject.src.model.helper import readMatrix, scikit_sparse_cholesky, getB

    
    matrix = readMatrix("apache2")
    b = getB(matrix)
    
    print(f"b: ---- \n {b} \n -----")
    print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")



    x = scikit_sparse_cholesky(matrix, b)
    print(f"x: ---- \n {x} \n -----")
