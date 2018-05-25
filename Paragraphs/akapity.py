class Akapity:
    def __init__(self, plik):
        self.plik = open(plik, 'r')
        self.wiersz = ""
        self.akapity = 0
        self.zakoncz = False

    def __iter__(self):
        return self

    def __next__(self):
        akapit = self.wiersz

        while True:
            self.wiersz = self.plik.readline()

            if self.wiersz == "\n":
                self.zakoncz = True
                break

            if "    " in self.wiersz:
                self.akapity += 1

            if self.akapity >= 2:
                break
            else:
                akapit += self.wiersz

        self.akapity = 1

        if self.zakoncz is False:
            return akapit
        else:
            raise StopIteration()
            plik.close()

    #def formatuj_akapit(self):

if __name__ == "__main__":
    akapity = Akapity('akapity.txt')

    iterator = iter(akapity)

    while True:
        try:
            i = iterator.__next__()
            print(i)
        except StopIteration:
            break