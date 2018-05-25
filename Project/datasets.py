from sklearn import datasets
import pandas as pd

if __name__ == "__main__":
    iris = datasets.load_iris()

    data = pd.DataFrame(iris.data, columns=iris.feature_names)
    data['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)
    data.to_csv('iris.csv')