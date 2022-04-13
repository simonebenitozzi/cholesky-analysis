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

    def __analyze(self, path):
        try:
            matrix = readMatrix(path)

            try:
                b = getB(matrix)

                # print(f"b: ---- \n {b} \n -----")
                # print(f"Matrix: \n ------------------- \n {matrix} \n ---------------- \n")

                # start time and memory track
                start_time = time.time()
                start_memory = computeMemoryUsage()

                x = scikit_sparse_cholesky(matrix, b)

                # stop time and memory track
                self.__memoryUsed = convert_size(
                    computeMemoryUsage() - start_memory)
                self.__timeTotal = time.time() - start_time

                # print(type(x))
                # print(f"x: ---- \n {x} \n -----")
            except Exception:
                print(f"Failed to read {self.__name}\n")
                raise Exception

        except Exception:
            print(f"Failed to read {self.__name}\n")
            raise Exception

        # compute distance
        self.__error = relativeError(x)
        print(f"Error: {self.__error}")

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
        print("####################### END #######################\n \n \n")
