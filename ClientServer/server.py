from xmlrpc.server import SimpleXMLRPCServer
import datetime


class KontaktySerwer:

    """klasa zawierająca funkcje operujące na danych"""

    def __init__(self):
        self.kontakty = {}
        self.wczytaj_kontakty()
        now = datetime.datetime.now()
        self.actual_data = \
            str(now.day) + '.' + str(now.month) + '.' + str(now.year)

    def wczytaj_kontakty(self):

        """wczytanie kontaktów z pliku"""

        with open('kontakty.txt', 'r') as dane:
            for kontakt in dane:
                self.kontakty[kontakt.split(':')[0]] = \
                    [kontakt.split(':')[1],
                     kontakt.split(':')[2],
                     kontakt.split(':')[3]]

    def wypisz_liste(self):

        """funkcja zwracająca listę do wypisania"""

        lista_wypisz = 'OSOBA           TELEFON           ' \
                       'EMAIL           Data\n\n'
        for kontakt in self.kontakty:
            lista_wypisz += self.wypisz_kontakt(kontakt)

        return lista_wypisz

    def wypisz_kontakt(self, osoba):

        """funkcja zwracająca kontakt do wypisania"""

        kontakt = ''
        kontakt += osoba
        kontakt += '    '
        kontakt += str(self.kontakty[osoba][0])
        kontakt += '    '
        kontakt += str(self.kontakty[osoba][1])
        kontakt += '    '
        kontakt += str(self.kontakty[osoba][2])
        kontakt += '\n'

        return kontakt

    def dodaj_kontakt(self, osoba, telefon, mail):

        """funkcja dodająca kontakt do pliku"""

        if osoba != '' and telefon != '' and mail != ''\
                and len(osoba.split()) == 2:
            if osoba not in self.kontakty:                  # dodawanie
                self.kontakty[osoba] = [telefon, mail, self.actual_data]
                dane = open('kontakty.txt', 'a')
                dane.write(osoba + ':' + telefon + ':'
                           + mail + ':' + self.actual_data + '\n')

            else:                                           # edycja
                dane = open("kontakty.txt", "r+")
                wiersze = dane.readlines()
                dane.seek(0)
                for wiersz in wiersze:
                    if osoba not in wiersz:
                        dane.write(wiersz)
                    else:
                        dane.write(osoba + ':' + telefon + ':'
                                   + mail + ':' + self.actual_data + '\n')
                dane.truncate()
                dane.close()

            return True
        return False

    def usun_kontakt(self, osoba):

        """funkcja usuwająca kontakt z pliku"""

        if osoba != '' and osoba in self.kontakty:
            del self.kontakty[osoba]

            dane = open("kontakty.txt", "r+")
            wiersze = dane.readlines()
            dane.seek(0)
            for wiersz in wiersze:
                if osoba not in wiersz:
                    dane.write(wiersz)
            dane.truncate()
            dane.close()

        return True

    def wyszukaj_kontakt(self, imie, nazwisko):

        """funkcja wyszukująca kontakt"""

        if imie != '' and nazwisko != '':
            osoba = imie + ' ' + nazwisko
            if osoba in self.kontakty:
                return self.wypisz_kontakt(osoba)
            else:
                return 'Nie ma takiego kontaktu'

        if imie != '' and nazwisko == '':     # po imieniu
            wyszukane_kontakty = ''
            for osoba in self.kontakty:
                if imie == str(osoba).split()[0]:
                    wyszukane_kontakty += self.wypisz_kontakt(osoba)

            if wyszukane_kontakty != '':
                return wyszukane_kontakty
            else:
                return 'Nie ma takiego kontaktu'

        if imie == '' and nazwisko != '':     # po nazwisku
            wyszukane_kontakty = ''
            for osoba in self.kontakty:
                if nazwisko == str(osoba).split()[1]:
                    wyszukane_kontakty += self.wypisz_kontakt(osoba)

            if wyszukane_kontakty != '':
                return wyszukane_kontakty
            else:
                return 'Nie ma takiego kontaktu'

        return ''


if __name__ == "__main__":
    server = SimpleXMLRPCServer(("localhost", 8888))
    kontakty_serwer = KontaktySerwer()
    server.register_function(kontakty_serwer.wypisz_liste)
    server.register_function(kontakty_serwer.dodaj_kontakt)
    server.register_function(kontakty_serwer.usun_kontakt)
    server.register_function(kontakty_serwer.wyszukaj_kontakt)
    server.serve_forever()
