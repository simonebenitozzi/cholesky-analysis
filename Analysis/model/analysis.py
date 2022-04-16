import pandas as pd

from Analysis.model.helper import read_data


def main():
    data1 = read_data("data.csv")
    data2 = read_data("data2.csv")
    data = pd.merge(data1, data2, left_on='Name', right_on='Name')
    print(data)


if __name__ == "__main__":
    main()
