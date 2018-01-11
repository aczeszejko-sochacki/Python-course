import numpy as np
from scipy import stats
from itertools import cycle
import matplotlib.pyplot as plt
plt.xkcd()


class Knn:

    """klasyfikator k-nearest neighbours"""

    def __init__(self, k):
        self.k = k
        self.test_target = None

    def knn_test(self, test_data, train_data, train_target):

        """funkcja klasyfikująca dane testowe"""

        sq1_sums = np.array([np.sum(test_data ** 2, axis=1)])
        sq2_sums = np.array([np.sum(train_data ** 2, axis=1)])
        mult = np.array(-2 * test_data.dot(np.transpose(train_data)))
        distances = np.array(np.transpose(sq1_sums) + sq2_sums + mult)

        nearest = train_target[distances.argsort()[:, :self.k]]

        self.test_target = np.concatenate(stats.mode(nearest, axis=1)[0])

    def draw_subplot(self, test_data, train_data, train_target, coef1, coef2):

        """funkcja tworząca wykres danych uczących
        i danych testowych z dwóch parametrów"""

        plt_colors = cycle(('blue', 'green', 'yellow'))

        labels = np.unique(train_target)

        for label in labels:
            color = next(plt_colors)

            indexes = np.where(train_target == label)

            x = train_data[indexes][:, coef1]
            y = train_data[indexes][:, coef2]

            plt.scatter(x, y, color=color, marker='o', s=10)

            new_indexes = np.where(self.test_target == label)

            x = test_data[new_indexes][:, coef1]
            y = test_data[new_indexes][:, coef2]

            plt.scatter(x, y, color=color, marker='x', s=50)

    def save_plot(self, test_data, train_data, train_target):

        """funkcja zapisaująca wykresy wszystkich możliwych
        kombinacji parametrów irysów dla danych uczących
        i testowych"""

        plt.figure(1)
        plt.subplot(231)
        self.draw_subplot(test_data, train_data, train_target, 0, 1)
        plt.subplot(232)
        self.draw_subplot(test_data, train_data, train_target, 2, 3)
        plt.figure(1)
        plt.subplot(233)
        self.draw_subplot(test_data, train_data, train_target, 0, 1)
        plt.subplot(234)
        self.draw_subplot(test_data, train_data, train_target, 2, 3)
        plt.subplot(235)
        self.draw_subplot(test_data, train_data, train_target, 0, 1)
        plt.subplot(236)
        self.draw_subplot(test_data, train_data, train_target, 2, 3)
        plt.tight_layout()
        plt.savefig('plot.png')
