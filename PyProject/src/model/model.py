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
    from PyProject.src.model.helper import readMatrix, scikit_sparse_cholesky

    matrix = readMatrix("apache2")

    
    print(f"\n Matrix Type: {type(matrix)} \n")
    print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")


    L = scikit_sparse_cholesky(matrix)
    

    print(L)
