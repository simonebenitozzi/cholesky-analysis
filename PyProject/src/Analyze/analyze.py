from asyncore import write
import time
from unicodedata import name
import re


from PyProject.src.Analyze.helper import computeMemoryUsage, convert_size, readMatrix, relativeError, scikit_sparse_cholesky, getB, writeCSV


class Analyze:
    def __init__(self):
        self.__name = None
        self.__error = None
        self.__memoryUsed = None
        self.__timeTotal = None
        writeCSV('Name', 'Error', 'Memory', 'Time')  # write header

    def __readMatrix(self, path):
        try:

            return readMatrix(path)

        except Exception:
            raise Exception(f"Failed to read {self.__name}\n")

    def __analyze(self, path):

        matrix = self.__readMatrix(path)  # read matrix
        b = getB(matrix)  # get b = A*xe

        # start time and memory track
        start_time = time.time()
        start_memory = computeMemoryUsage()
        ###########################

        # CHOLESKY
        try:
            x = scikit_sparse_cholesky(matrix, b)
        except Exception:
            raise Exception(f"Failed to execute cholesky on {self.__name}\n")
        ##########################

        # stop time and memory track
        self.__memoryUsed = computeMemoryUsage() - start_memory
        self.__timeTotal = time.time() - start_time
        ##########################

        # compute distance
        self.__error = relativeError(x)

    def __setName(self, name):
        self.__name = name.split(".mtx")[0]

    def startAnalyze(self, path, name):
        self.__setName(name)

        # Analysis
        self.__analyze(path)

        # write data
        writeCSV(self.__name, self.__error,
                 self.__memoryUsed, self.__timeTotal)

        print(f"Name: {self.__name}")
        print(f"Memory: {self.__memoryUsed}")
        print(f"Seconds: {self.__timeTotal} \n")
        print(f"Error: {self.__error}")
        print("####################### END #######################\n \n \n")
