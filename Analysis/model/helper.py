import os

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from matplotlib.pyplot import figure
from matplotlib_inline import config
from matplotlib_inline.config import InlineBackend
from sklearn.linear_model import LinearRegression

from Analysis.model.costants import X_LABEL, Y_LABEL, LOG_SCALE

plt.style.context('fivethirtyeight')


def get_data_sorted(name, data):
    """
    Takes the dataset and the name of column on which it sorts
    return python, matlab dataset
    """
    data = data.sort_values(by=[name])  # sort sulle dimensioni delle matrici in ordine crescente
    data_python = data.loc[data['Language'] == 1]
    data_matlab = data.loc[data['Language'] == 0]
    return data_python, data_matlab


def read_data(name):
    from Analysis.resources.costants import RESOURCES_DIRECTORY
    path = os.path.join(RESOURCES_DIRECTORY, name)
    return pd.read_csv(path)


def write_data(df, name):
    from Analysis.resources.costants import RESOURCES_DIRECTORY
    path = os.path.join(RESOURCES_DIRECTORY, name)
    df.to_csv(path, index=False)


# TODO: legend1 e legend2 possono essere rimossi! basta usare x_name e y_name
def plot(labels, data_py, data_matlab, x_name, y_name, title, legend1, legend2, **keywords):
    figure(figsize=(20, 6), dpi=80)
    title = title + " " + "(Line Plot)"

    plt.plot(labels, data_py, label=legend1, linestyle="-")
    plt.plot(labels, data_matlab, label=legend2, linestyle="--")
    show(x_name, y_name, title, **keywords)


def bar_plot(labels, data_py, data_matlab, x_name, y_name, title, legend1, legend2, **keywords):
    figure(figsize=(20, 6), dpi=80)
    title = title + " " + "(Bar Plot)"

    x_axis = np.arange(len(labels))

    # Multi bar Chart

    plt.bar(x_axis - 0.2, data_py, width=0.4, label=legend1)
    plt.bar(x_axis + 0.2, data_matlab, width=0.4, label=legend2)

    # Xticks

    plt.xticks(x_axis, labels)
    show(x_name, y_name, title, **keywords)


def show(x_name, y_name, title, **keywords):
    x_label, y_label = "", ""
    if X_LABEL in keywords.keys():
        x_label = f"({keywords[X_LABEL]})"
    if Y_LABEL in keywords.keys():
        y_label = f"({keywords[Y_LABEL]})"
    if LOG_SCALE in keywords.keys():
        plt.yscale('log')  # logarithmic scale

    plt.xlabel(f"{x_name} {x_label}", labelpad=15, fontsize=12, color="#333533")
    plt.ylabel(f"{y_name} {y_label}", labelpad=15, fontsize=12, color="#333533")
    plt.title(title, fontsize=18, color="#333533", pad=35)

    # removing axes from the figure
    plt.gca().spines['right'].set_visible(False)
    plt.gca().spines['top'].set_visible(False)
    plt.legend(loc='upper center', ncol=2, frameon=False)
    plt.show()


def correlation(x, y, x_name, y_name):
    figure(figsize=(20, 6), dpi=80)
    title = f"Scatter-plot variables '{x_name}' and '{y_name}'"
    my_rho = np.corrcoef(x, y)  # Correlation Coefficient
    print(my_rho)

    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)

    # Creatoing a linear regression model and fitting the data to the model
    model = LinearRegression()
    model.fit(x, y)

    # Now, predicting the y values according to the model
    y_line = model.predict(x)

    # Printing thr coffecient/parameter of the resulted line
    print(f"The parameters of the line: {model.coef_}")

    # Plotting the data points and the best fit line
    plt.scatter(x, y)
    plt.plot(x, y_line, 'r', label=f"Correlation Coefficient {my_rho[0][1]}")

    show(x_name, y_name, title)
