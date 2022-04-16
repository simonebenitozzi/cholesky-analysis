import os
import sys
from pathlib import Path

import pandas as pd

from Analysis.model.helper import read_data

myDir = os.getcwd()
sys.path.append(myDir)
path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)


def main():

    data1 = read_data("data.csv")
    data2 = read_data("data2.csv")
    data = data1.join(data2)

    print(data.head())



if __name__ == "__main__":
    main()
