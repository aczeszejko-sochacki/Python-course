import unittest
from kontakty import Kontakty


class Testy(unittest.TestCase):

    kontakty = Kontakty()

    def test_wypisz_kontakt(self):
        self.assertEqual(self.kontakty.wypisz_kontakt('Bob Bil'),
                         'Bob Bil    123456780    bobbi@net.net    30.11.2017\n\n')

    def test2_wypisz_kontakt(self):
        self.assertEqual(self.kontakty.wypisz_kontakt('Ala Alf'),
                         'Ala Alf    761918782    alalf@mymail.pl    29.11.2017\n\n')


if __name__ == "__main__":
    unittest.main()
