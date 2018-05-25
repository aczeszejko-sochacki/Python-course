import numpy as np
import matplotlib.pyplot as plt
from itertools import cycle
plt.xkcd()


class BasicPlot:

    """klasa tworząca wykres danych uczących"""

    def basic_subplot(self, train_data, train_target, coef1, coef2):

        """funkcja tworząca wykres danych uczących
        z dwóch parametrów"""

        plt_colors = cycle(('blue', 'green', 'yellow'))

        labels = np.unique(train_target)

        for label in labels:
            color = next(plt_colors)

            indexes = np.where(train_target == label)

            x = train_data[indexes][:, coef1]
            y = train_data[indexes][:, coef2]

            plt.scatter(x, y, color=color, marker='o', s=10)

    def save_basic_plot(self, train_data, train_target):

        """funkcja zapisaująca wykresy wszystkich możliwych
        kombinacji parametrów irysów"""

        plt.figure(1)
        plt.subplot(231)
        self.basic_subplot(train_data, train_target, 0, 1)
        plt.subplot(232)
        self.basic_subplot(train_data, train_target, 0, 2)
        plt.figure(1)
        plt.subplot(233)
        self.basic_subplot(train_data, train_target, 0, 3)
        plt.subplot(234)
        self.basic_subplot(train_data, train_target, 1, 2)
        plt.subplot(235)
        self.basic_subplot(train_data, train_target, 1, 3)
        plt.subplot(236)
        self.basic_subplot(train_data, train_target, 2, 3)
        plt.tight_layout()
        plt.savefig('plot.png')
