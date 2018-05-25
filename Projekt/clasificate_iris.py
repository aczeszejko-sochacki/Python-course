from knn import Knn
import numpy as np
import threading


class Target:
    def __init__(self, data, target):
        self.data = data
        self.target = target

    def clasificate_all_iris(self, sl, sw, pl, pw, n_neighbours):
        sl, sw, pl, pw, n_neighbours = \
            sl.split(), sw.split(), pl.split(), pw.split(), \
            n_neighbours.split()

        if len(sl) == len(sw) == len(pl) == len(pw) == \
            len(n_neighbours):

            d = len(sl)

            threads = {}

            for index in range(d):
                threads[str('index')] = threading.Thread(target=self.clasificate_iris(sl[index], sw[index], pl[index], pw[index], n_neighbours[index]))
                threads[str('index')].start()
            for index in range(d):
                threads[str('index')].join()

            return True

        return False

    def clasificate_iris(self, sl, sw, pl, pw, n_neighbours):

        """funkcja klasyfikująca kwiat o podanych parametrach
        i danej liczbie sąsiadów"""

        if pw.replace('.', '', 1).isdigit() \
                and pl.replace('.', '', 1).isdigit() \
                and sw.replace('.', '', 1).isdigit() \
                and sl.replace('.', '', 1).isdigit() \
                and n_neighbours.isdigit():

            pw, pl, sw, sl, n_neighbours\
                = float(pw), float(pl), float(sw),\
                  float(sl), int(n_neighbours)

            if sl <= 8 and sw <= 8 and pl <= 8 and pw <= 8\
                    and 0 <= sl and 0 <= sw and 0 <= pl and 0 <= pw:

                knn = Knn(n_neighbours)
                knn.knn_test(np.array([[pw, pl, sw, sl]]), self.data,
                             self.target)
                knn.save_plot(np.array([[pw, pl, sw, sl]]), self.data,
                              self.target)

    def clasificate_iris_to_test(self, sl, sw, pl, pw, n_neighbours):

        """funkcja klasyfikująca kwiat o podanych parametrach
        i danej liczbie sąsiadów"""

        if pw.replace('.', '', 1).isdigit() \
                and pl.replace('.', '', 1).isdigit() \
                and sw.replace('.', '', 1).isdigit() \
                and sl.replace('.', '', 1).isdigit() \
                and n_neighbours.isdigit():

            pw, pl, sw, sl, n_neighbours\
                = float(pw), float(pl), float(sw),\
                  float(sl), int(n_neighbours)

            if sl <= 8 and sw <= 8 and pl <= 8 and pw <= 8\
                    and 0 <= sl and 0 <= sw and 0 <= pl and 0 <= pw:

                knn = Knn(n_neighbours)
                knn.knn_test(np.array([[pw, pl, sw, sl]]), self.data,
                             self.target)
                knn.save_plot(np.array([[pw, pl, sw, sl]]), self.data,
                              self.target)
                return True
            else:
                return False
        else:
            return False

