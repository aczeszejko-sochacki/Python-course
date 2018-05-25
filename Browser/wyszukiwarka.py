from bs4 import BeautifulSoup

class Wyszukiwarka:
    def __init__(self, lista_stron):
        self.lista_slownikow = {}
        self.lista_stron = lista_stron
        self.wystapienia = {}

    def przegladaj_strone(self, strona):
        with open(str(strona) + ".html") as data:
            file_html = data.read()
            data.close()
            soup = BeautifulSoup(file_html, 'html.parser')
            text = soup.get_text()
            text = text.replace('\n', ' ')
            text = text.split()

        slowa = {}

        for klucz in text:
            if klucz.isalpha():
                if klucz in slowa:
                    slowa[klucz] = slowa[klucz] + 1
                else:
                    slowa[klucz] = 1

        self.lista_slownikow[strona] = slowa

    def przegladnij_wszystkie(self):
        for strona in self.lista_stron:
            self.przegladaj_strone(strona)

    def zbuduj_wyszukiwarke(self):
        for strona in self.lista_slownikow:
            for slowo in self.lista_slownikow[strona]:
                if slowo in self.wystapienia:
                    self.wystapienia[slowo].append((self.lista_slownikow[strona][slowo], strona))
                else:
                    self.wystapienia[slowo] = [(self.lista_slownikow[strona][slowo], strona)]

        for klucz in self.wystapienia:
            self.wystapienia[klucz].sort()
            self.wystapienia[klucz].reverse()

        print(self.wystapienia)

    def zapytanie(self, wyraz):
        strony = []

        if(wyraz not in self.wystapienia):
            print('Nie ma takiego klucza.')
        else:
            for liczba, strona in self.wystapienia[wyraz]:
                strony.append(strona)

        print(strony)