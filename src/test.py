from sklearn import datasets
from main import save_myConvexHull

def main():
    testCases = [
            (datasets.load_iris(), "Iris Dataset", 0, 1),
            (datasets.load_iris(), "Iris Dataset", 2, 3),
            (datasets.load_wine(), "Wine Dataset", 0, 1),
            (datasets.load_breast_cancer(), "Breast Cancer Dataset", 9, 1)
            ]

    for case in testCases:
        save_myConvexHull(case[0], case[1], case[2], case[3], "test")


if __name__ == "__main__":
    main()
