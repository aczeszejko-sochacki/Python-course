import time
import Doskonale
import matplotlib.pyplot as plt


class DoskonalaIter:
    def __init__(self, n):
        self.i = 1
        self.n = n
        self.doskonale = []

    def __iter__(self):
        return self

    def __next__(self):
        if self.i < self.n:
            if sum([dzielnik for dzielnik in range(1, self.i // 2 + 1) if self.i % dzielnik == 0]) == self.i:
                self.doskonale.append(self.i)

            self.i += 1
            return self.doskonale

        else:
            raise StopIteration()


if __name__ == "__main__":
    x = ["doskonale_iter", "doskonale_fun", "doskonale_skl"]
    y = []


    tp = time.perf_counter()

    doskonale = DoskonalaIter(10000)
    iterator = iter(doskonale)

    while True:
        try:
            i = iterator.__next__()
        except StopIteration:
            print(i)
            break

    tk = time.perf_counter()
    y.append(tk - tp)

    tp = time.perf_counter()
    Doskonale.doskonale_skladana(10000)
    tk = time.perf_counter()
    y.append(tk - tp)

    tp = time.perf_counter()
    Doskonale.doskonale_funkcyjna(10000)
    tk = time.perf_counter()
    y.append(tk - tp)

    plt.scatter(x, y)
    plt.show()
    plt.savefig("czasy.png")
