from asyncore import write
import time
from unicodedata import name
import re


from PyProject.src.Analyze.helper import convert_size, endTrackMemory, readMatrix, relativeError, scikit_sparse_cholesky, getB, startTrackMemory, writeCSV


class Analyze:
    def __init__(self):
        self.__name = None
        self.__error = None
        self.__memoryUsed = None
        self.__timeTotal = None
        writeCSV('Name', 'Error', 'Memory', 'Time')  # write header

    def __analyze(self, path):

        matrix = readMatrix(path)  # read matrix
        b = getB(matrix)  # get b = A*xe

        # start time and memory track
        start_time = time.time()
        startTrackMemory()
        ###########################

        # CHOLESKY
        x = scikit_sparse_cholesky(matrix, b)
        ##########################

        # stop time and memory track
        self.__memoryUsed = convert_size(endTrackMemory())
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
