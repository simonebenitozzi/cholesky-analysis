from asyncore import write
import time
from unicodedata import name


from PyProject.src.Analyze.helper import computeMemoryUsage, convert_size, readMatrix, relativeError, scikit_sparse_cholesky, getB, writeCSV


class Analyze:
    def __init__(self):
        self.__name = None
        self.__error = None
        writeCSV('Name', 'Error', 'Memory', 'Time')  # write header

    def __analyze(self):
        matrix = readMatrix(self.__name)
        b = getB(matrix)

        # print(f"b: ---- \n {b} \n -----")
        # print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")

        x = scikit_sparse_cholesky(matrix, b)
        # print(type(x))
        # print(f"x: ---- \n {x} \n -----")

        # compute distance
        self.__error = relativeError(x)
        # print(f"DISTANCE: {ERROR} \n")

    def __setName(self, name):
        self.__name = name

    def startAnalyze(self, name):
        self.__setName(name)

        # start
        start_time = time.time()
        start_memory = computeMemoryUsage()

        # Analysis
        self.__analyze()

        # stop
        memoryUsed = convert_size(computeMemoryUsage() - start_memory)
        timeTotal = time.time() - start_time

        # write data
        writeCSV(name, self.__error, memoryUsed, timeTotal)

        print(
            f"--------------------------- {name} ------------------------ \n")
        print(f"--- memory --- {memoryUsed} \n")
        print(f"--- seconds ---  {timeTotal}")
        print(f"---------------------------        ------------------------ \n")
