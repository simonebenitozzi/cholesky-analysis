from asyncore import write
import time
from unicodedata import name
import re


from PyProject.src.Analyze.helper import computeMemoryUsage, convert_size, readMatrix, relativeError, scikit_sparse_cholesky, getB, writeCSV


class Analyze:
    def __init__(self):
        self.__name = None
        self.__path = None
        self.__error = None
        writeCSV('Name', 'Error', 'Memory', 'Time')  # write header

    def __analyze(self):
        try:
            matrix = readMatrix(self.__path)
            b = getB(matrix)

            # print(f"b: ---- \n {b} \n -----")
            # print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")

            x = scikit_sparse_cholesky(matrix, b)
            # print(type(x))
            # print(f"x: ---- \n {x} \n -----")
        except Exception:
            print(f"Failed to analyze {self.__name}\n")
            raise Exception

        # compute distance
        self.__error = relativeError(x)
        # print(f"DISTANCE: {ERROR} \n")

    def __setNameAndPath(self, path):
        self.__path = path
        self.__name = re.search("(\w+).mtx", path).group(1)
        print(f"Name: {self.__name}")

    def startAnalyze(self, path):
        self.__setNameAndPath(path)

        # start
        start_time = time.time()
        start_memory = computeMemoryUsage()

        # Analysis
        self.__analyze()

        # stop
        memoryUsed = convert_size(computeMemoryUsage() - start_memory)
        timeTotal = time.time() - start_time

        # write data
        writeCSV(self.__name, self.__error, memoryUsed, timeTotal)

        print(f"Memory: {memoryUsed} \n")
        print(f"Seconds: {timeTotal} \n")
        print("####################### END #######################\n \n \n")
