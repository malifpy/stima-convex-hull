import re
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import datasets
from myConvexHull import myConvexHull

def main():
    print("Convex Hull Algorithm Interactive Mode")
    print("[1] START")
    print("[2] EXIT")
    q_loop = input("Input Choice: ").lower()
    while(q_loop != "2" and q_loop != "exit"):
        data, title, x_idx, y_idx = query()
        display_save_myConvexHull(data, title, x_idx, y_idx)

        print("[1] START")
        print("[2] EXIT")
        q_loop = input("Input Choice: ").lower()
    #fig.savefig(f'IrisDataset.png')

def query():
    data_dummy = [
            (datasets.load_iris(), "Iris Dataset"),
            (datasets.load_wine(), "Wine Dataset"),
            (datasets.load_breast_cancer(), "Breast Cancer Dataset")
            ]
    for idx, dt in enumerate(data_dummy):
        print(f"[{idx + 1}] {dt[1]}")

    chosen_data_idx = int(input("Data Pilihan: "))
    while(chosen_data_idx < 1 or chosen_data_idx > len(data_dummy)):
        chosen_data_idx = int(input("Data Pilihan: "))

    chosen_data = data_dummy[chosen_data_idx - 1][0]

    for idx, ft in enumerate(chosen_data.feature_names):
        print(f"[{idx + 1}] {ft}")

    chosen_X = int(input("Sumbu X Pilihan: "))
    while(chosen_X < 1 or chosen_X > len(chosen_data.feature_names)):
        chosen_X = int(input("Sumbu X Pilihan: "))

    chosen_Y = int(input("Sumbu Y Pilihan: "))
    while(chosen_Y < 1 or chosen_Y > len(chosen_data.feature_names) or chosen_Y == chosen_X):
        chosen_Y = int(input("Sumbu Y Pilihan: "))

    return chosen_data, data_dummy[chosen_data_idx - 1][1], chosen_X - 1, chosen_Y - 1

def display_save_myConvexHull(data, dataset_name, x_index, y_index, directory="img"):
    fig, ax = fig_myConvexHull(data, dataset_name, x_index, y_index)
    plt.show()
    q_save = input("Save Figure [Y/n]? ").lower()
    if (q_save == "" or q_save == "Y"):
        filename = input("File Name? ")
        if(not filename):
            filename = re.sub("[^a-zA-Z0-9]", "_", ax.get_title())
        fig.savefig(f"{directory}/{filename}.png")
        print(f"Saved in: {directory}/{filename}.png")
    plt.close(fig)

def display_myConvexHull(data, dataset_name, x_index, y_index):
    fig, ax = fig_myConvexHull(data, dataset_name, x_index, y_index)
    plt.show()
    plt.close(fig)

def save_myConvexHull(data, dataset_name, x_index, y_index, directory="img", filename=""):
    fig, ax = fig_myConvexHull(data, dataset_name, x_index, y_index)
    if(not filename):
        filename = re.sub("[^a-zA-Z0-9]", "_", ax.get_title())
    fig.savefig(f"{directory}/{filename}.png")
    print(f"Saved in: {directory}/{filename}.png")
    plt.close(fig)

def fig_myConvexHull(data, dataset_name, x_index, y_index):

    # Create a DataFrame
    df = pd.DataFrame(data.data, columns=data.feature_names)
    df['Target'] = pd.DataFrame(data.target)

    # Visualisasi Hasil ConvexHull
    fig, ax = plt.subplots(figsize = (10, 6))

    x_axis = re.sub("\(.*\)", "", data.feature_names[x_index]).strip().title();
    y_axis = re.sub("\(.*\)", "", data.feature_names[y_index]).strip().title();
    ax.set_title(f'{dataset_name}: {x_axis} vs {y_axis}')

    ax.set_xlabel(data.feature_names[x_index])
    ax.set_ylabel(data.feature_names[y_index])

    # Iterating per-target
    for i in range(len(data.target_names)):

        bucket = df[df['Target'] == i]
        bucket = bucket.iloc[:,[x_index,y_index]].values
        target_label = str(data.target_names[i]).title()

        hull = myConvexHull(bucket) # Algoritma Sendiri
        print(target_label, len(hull), "Convex Points")

        c_normal, c_dark = get_random_color()

        ax.scatter(bucket[:, 0], bucket[:, 1], label=target_label, color=c_normal)

        for simpul in hull:
            x = [simpul[0][0], simpul[1][0]]
            y = [simpul[0][1], simpul[1][1]]
            ax.plot(x, y, color=c_dark)


    ax.legend()

    return fig, ax

def get_random_color():
    c = np.random.rand(3, ) * 3 / 4
    return c, c * 5/8

if __name__ == "__main__":
    main()
