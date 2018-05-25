from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.config import Config
import kivy
import xmlrpc.client

kivy.require('1.10.0')

Config.set('graphics', 'resizable', False)
Config.set('graphics', 'width', '800')
Config.set('graphics', 'height', '500')


class Kontakty(GridLayout):

    """klasa zawierająca funkcje operujące na danych"""

    def __init__(self):
        GridLayout.__init__(self)

    def lista(self):

        """wypisanie listy w głównym oknie"""

        with xmlrpc.client.ServerProxy("http://localhost:8888/") as proxy:
            self.ids.okno.text = proxy.wypisz_liste()

    def dodaj_kontakt(self, osoba, telefon, mail):

        """funkcja dodająca kontakt do pliku"""

        with xmlrpc.client.ServerProxy("http://localhost:8888/") as proxy:
            proxy.dodaj_kontakt(osoba, telefon, mail)
            self.ids.osoba.text = ''
            self.ids.telefon.text = ''
            self.ids.email.text = ''

    def usun_kontakt(self, osoba):

        """funkcja usuwająca kontakt z pliku"""

        with xmlrpc.client.ServerProxy("http://localhost:8888/") as proxy:
            proxy.usun_kontakt(osoba)
            self.ids.usun_osoba.text = ''

    def wyszukaj_kontakt(self, imie, nazwisko):

        """funkcja wyszukująca kontakt"""

        with xmlrpc.client.ServerProxy("http://localhost:8888/") as proxy:
            self.ids.okno.text = proxy.wyszukaj_kontakt(imie, nazwisko)
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
