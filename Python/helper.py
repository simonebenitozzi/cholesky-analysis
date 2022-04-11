from scipy.io import mmread


def readMatrix(filename):
    matrix = mmread(f'Matrix/{filename}.mtx')
    return matrix
