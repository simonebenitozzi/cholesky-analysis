from scipy.io import mmread


def readMatrix(filename):
    return mmread(f'Matrix/{filename}.mtx')
