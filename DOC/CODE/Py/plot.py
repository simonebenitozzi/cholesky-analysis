def plot(labels, data_py, data_matlab, x_name, y_name, title, legend1, legend2, path, **keywords):
    figure(figsize=(20, 6), dpi=80)
    title = title + " " + "(Line Plot)"

    plt.plot(labels, data_py, label=legend1, linestyle="-")
    plt.plot(labels, data_matlab, label=legend2, linestyle="--")
    show(x_name, y_name, title, path, **keywords)


def bar_plot(labels, data_py, data_matlab, x_name, y_name, title, legend1, legend2, path, **keywords):
    figure(figsize=(20, 6), dpi=80)
    title = title + " " + "(Bar Plot)"

    x_axis = np.arange(len(labels))

    # Multi bar Chart

    plt.bar(x_axis - 0.2, data_py, width=0.4, label=legend1)
    plt.bar(x_axis + 0.2, data_matlab, width=0.4, label=legend2)

    # Xticks

    plt.xticks(x_axis, labels)
    show(x_name, y_name, title, path, **keywords)


def show(x_name, y_name, title, path, **keywords):
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

    plt.savefig(path)
    plt.show()