import time


def doskonale_skladana(n):
    doskonale = [x for x in range(2, n) if sum([dzielnik for dzielnik in range(1, x // 2 + 1)
                                                if x % dzielnik == 0]) == x]
    return doskonale


def doskonale_funkcyjna(n):
    doskonale = list(filter(lambda x: sum(list(filter(lambda dzielnik: x % dzielnik == 0, range(1, x // 2 + 1)))) == x,
                            range(2, n)))
    return doskonale

if __name__ == "__main__":
    tp = time.perf_counter()
    print(doskonale_skladana(10000))
    tk = time.perf_counter()
    print(tk - tp)
    tp = time.perf_counter()
    print(doskonale_funkcyjna(10000))
    tk =time.perf_counter()
    print(tk - tp)
