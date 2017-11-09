class Zdania:
    def __init__(self, plik):
        with open(plik, "r") as plik:
            tekst = plik.read()
            tekst = tekst.replace('\n', '')
            self.zdania = tekst.split()
            plik.close()

        self.index = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.zdania) - 1:
            raise StopIteration()
        else:
            self.index += 1
            return self.zdania[self.index]

    def korekta(self, zdanie):
        zdanie = zdanie.capitalize()

        if zdanie.endswith(".") is False:
            zdanie += "."

        return zdanie


if __name__ == "__main__":
    test = Zdania("zdania.txt")
    iterator = iter(test)
    surowy_wynik = []

    while True:
        try:
            i = iterator.__next__()
            surowy_wynik.append(i)
        except StopIteration:
            break

    print(list(map(test.korekta, surowy_wynik)))