from pathlib import Path
import sys
import os

myDir = os.getcwd()
sys.path.append(myDir)
path = Path(myDir)
a = str(path.parent.absolute())
sys.path.append(a)


if __name__ == "__main__":

    from PyProject.src.Analyze.analyze import Analyze
    from PyProject.src.model.helper import getListOfFiles

    analyzing = Analyze()

    # Get the list of all files and directories
    path = "Matrix/"
    dir_list = getListOfFiles(path)
    for name in dir_list:
        print(f"path: {name} \n")
        try:
            analyzing.startAnalyze(name)
        except Exception:
            continue
