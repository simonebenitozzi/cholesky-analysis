from pathlib import Path
import pandas as pd
import os
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)


def main():
    from Analysis.resources.costants import RESOURCES_DIRECTORY
    path = os.path.join(RESOURCES_DIRECTORY, "Py.csv")
    data = pd.read_csv(path)
    print(data.head())


if __name__ == "__main__":
    main()
