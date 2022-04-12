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

    analyzing = Analyze()

    # Get the list of all files and directories
    path = "Matrix/"
    dir_list = os.listdir(path)
    for name in dir_list:
        analyzing.startAnalyze(name)
