import html.parser


class Wyszukiwarka(html.parser.HTMLParser):
    ciagi = {}

    def handle_data(self, data):
        if data not in self.ciagi:
            self.ciagi[data] = 1
        else:
            self.ciagi[data] = self.ciagi[data] + 1


def przegladaj_strone(strona):
    parser = Wyszukiwarka()

    with open(str(strona) + ".html") as data:
        parser.feed(data.read())
        data.close()

    slowa = {}

    for klucz in parser.ciagi.keys():
        nowe_klucze = klucz.split()

        for i in nowe_klucze:
            if i.isalpha():
                if i in slowa.keys():
                    slowa[i] = slowa[i] + parser.ciagi[klucz]
                else:
                    slowa[i] = parser.ciagi[klucz]

    return slowa


def zbuduj_wyszukiwarke(lista_slownikow):
    wyszukiwarka = {}

    for strona in lista_slownikow.keys():
        for slowo in lista_slownikow[strona]:
            if slowo in wyszukiwarka.keys():
                wyszukiwarka[slowo].append((lista_slownikow[strona][slowo], strona))
            else:
                wyszukiwarka[slowo] = [(lista_slownikow[strona][slowo], strona)]

    for klucz in wyszukiwarka.keys():
        wyszukiwarka[klucz].sort()
        wyszukiwarka[klucz].reverse()

    return wyszukiwarka


if __name__ == "__main__":
    lista_stron = ["pythonhtmlparser", "pythonhtml", "structuredmarkup"]
    lista_slownikow = {}

    for strona in lista_stron:
        lista_slownikow[strona] = przegladaj_strone(strona)

    print(lista_slownikow)
    print(zbuduj_wyszukiwarke(lista_slownikow))
