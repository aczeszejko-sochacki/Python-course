from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import datetime
import kivy
kivy.require('1.10.0')

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')


class Kontakty(GridLayout):

    """klasa zawierająca funkcje operujące na danych"""

    def __init__(self):
        GridLayout.__init__(self)
        self.kontakty = {}
        self.wczytaj_kontakty()
        now = datetime.datetime.now()
        self.actual_data = \
            str(now.day) + '.' + str(now.month) + '.' + str(now.year)

    def wczytaj_kontakty(self):

        """wczytanie kontaktów z pliku"""

        dane = open('kontakty.txt', 'r')
        while True:
            kontakt = dane.readline()

            if len(kontakt) == 0:
                break

            self.kontakty[kontakt.split(':')[0]] = [kontakt.split(':')[1],
                                                    kontakt.split(':')[2],
                                                    kontakt.split(':')[3]]
        dane.close()

    def lista(self):

        """wypisanie listy w głównym oknie"""

        self.ids.okno.text = self.wypisz_liste()

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
            self.kontakty[osoba] = [telefon, mail, self.actual_data]
            self.ids.osoba.text = ''
            self.ids.telefon.text = ''
            self.ids.email.text = ''

            if osoba not in self.kontakty:                  # dodawanie
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

    def usun_kontakt(self, osoba):

        """funkcja usuwająca kontakt z pliku"""

        if osoba != '' and osoba in self.kontakty:
            del self.kontakty[osoba]
            self.ids.usun_osoba.text = ''

            dane = open("kontakty.txt", "r+")
            wiersze = dane.readlines()
            dane.seek(0)
            for wiersz in wiersze:
                if osoba not in wiersz:
                    dane.write(wiersz)
            dane.truncate()
            dane.close()

    def wyszukaj_kontakt(self, imie, nazwisko):

        """funkcja wyszukująca kontakt"""

        if imie != '' and nazwisko != '':
            osoba = imie + ' ' + nazwisko
            if osoba in self.kontakty:
                self.ids.okno.text = self.wypisz_kontakt(osoba)
            else:
                self.ids.okno.text = 'Nie ma takiego kontaktu'

        if imie != '' and nazwisko == '':     # po imieniu
            wyszukane_kontakty = ''
            for osoba in self.kontakty:
                if imie == str(osoba).split()[0]:
                    wyszukane_kontakty += self.wypisz_kontakt(osoba)

            if wyszukane_kontakty != '':
                self.ids.okno.text = wyszukane_kontakty
            else:
                self.ids.ono.text = 'Nie ma takiego kontaktu'

        if imie == '' and nazwisko != '':     # po nazwisku
            wyszukane_kontakty = ''
            for osoba in self.kontakty:
                if nazwisko == str(osoba).split()[1]:
                    wyszukane_kontakty += self.wypisz_kontakt(osoba)

            if wyszukane_kontakty != '':
                self.ids.okno.text = wyszukane_kontakty
            else:
                self.ids.ono.text = 'Nie ma takiego kontaktu'

        if imie != '' or nazwisko != '':     # po imieniu i nazwisku
            self.ids.imie.text = ''
            self.ids.nazwisko.text = ''


class KontaktyApp(App):

    """klasa inicjalizująca aplikację"""

    def build(self):

        """funkcja inicjalizująca aplikację"""
        return Kontakty()


if __name__ == "__main__":
    kontakty_app = KontaktyApp()
    kontakty_app.run()
