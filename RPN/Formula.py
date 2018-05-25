"""Protokol:

Wprowadznie wartosci postaci:

((True, p), (True, True), (and, and), (False, q), (imp, imp))

1. Postac ONP
2. Dla wartosci zawsze prawdziwej lub falszywej: (True, True) lub (False, False)
3. Dla zmiennej logicznej: (>>wartosc logiczna<<, >>nazwa zmiennej<<)
4. Dla operatora logicznego: (>>operator<<, >>operator<<)
"""

"""klasa glowna"""
class Formula:
    zdania = []                                      #wylacznie nazwy zmiennych i operatory
    zmienne = []                                     #wylacznie wartosci logiczne i operatory
    stos = []                                         #do implementacji ONP

    def __init__(self, *zdania):                      #nieznana liczba zdan i operatorow
        for p in zdania:
            self.zdania.append(p[1])
            self.zmienne.append(p[0])

    def oblicz(self, zmienne):
        for p in zmienne:                              #budujemy ONP
            if p == 'and':
                x = self.stos.pop()
                y = self.stos.pop()
                koniunkcja = Koniunkcja()
                self.stos.append(koniunkcja.oblicz(x, y))
            elif p == 'or':
                x = self.stos.pop()
                y = self.stos.pop()
                alternatywa = Alternatywa()
                self.stos.append(alternatywa.oblicz(x, y))
            elif p == 'imp':
                x = self.stos.pop()
                y = self.stos.pop()
                implikacja = Implikacja()
                self.stos.append(implikacja.oblicz(x, y))
            elif p == 'wtw':
                x = self.stos.pop()
                y = self.stos.pop()
                rownowaznosc = Rownowaznosc()
                self.stos.append(rownowaznosc.oblicz(x, y))
            elif p == 'not':
                x = self.stos.pop()
                negacja = Negacja()
                self.stos.append(negacja.oblicz(x))
            else:
                self.stos.append(p)
        return self.stos.pop()

    def __str__(self):
        for p in self.zdania:                                        #budujemy ONP
            if p == 'and':
                x = self.stos.pop()
                y = self.stos.pop()
                koniunkcja = Koniunkcja()
                self.stos.append(koniunkcja.__str__(x, y))
            elif p == 'or':
                x = self.stos.pop()
                y = self.stos.pop()
                alternatywa = Alternatywa()
                self.stos.append(alternatywa.__str__(x, y))
            elif p == 'imp':
                x = self.stos.pop()
                y = self.stos.pop()
                implikacja = Implikacja()
                self.stos.append(implikacja.__str__(x, y))
            elif p == 'wtw':
                x = self.stos.pop()
                y = self.stos.pop()
                rownowaznosc = Rownowaznosc()
                self.stos.append(rownowaznosc.__str__(x, y))
            elif p == 'not':
                x = self.stos.pop()
                negacja = Negacja()
                self.stos.append(negacja.__str__(x))
            else:
                self.stos.append(p)

        return self.stos.pop()

    binarna = []

    def bin(self, n, d):                                        #konwersja na binarna(dopelniamy zerami z lewej)
        while n > 0:
            if n % 2 == 1:
                self.binarna.insert(0, 1)
            else:
                self.binarna.insert(0, 0)
            n //= 2

        while len(self.binarna) < d:
            self.binarna.insert(0, 0)

    def tautologia(self):
        baza = []                            #baza roznych zdan

        for zdanie in self.zdania:                #wypelniamy baze
            if zdanie not in baza and zdanie not in [True, False, 'and', 'or', 'imp', 'wtw', 'not']:
                baza.append(zdanie)

        d = len(baza)
        d2 = len(self.zmienne)
        po = 2**d

        for i in range(po):                                         #wszystkie mozliwe waluacje
            self.binarna = []                                        #czyscimy binarna
            self.bin(i, d)
            nowe_zmienne = []

            for zmienna in self.zmienne:
                if zmienna in [True, False]:
                    nowe_zmienne.append(False)
                else:
                    nowe_zmienne.append(zmienna)

            for j in range(d):                                            #zmieniamy wartosci logiczne
                if self.binarna[j] == 1:
                    litera_do_zmiany = baza[j]

                    for k in range(d2):                                   #znajdujemy zdania do zmiany
                        if self.zdania[k] == litera_do_zmiany:
                            nowe_zmienne[k] = True

            if self.oblicz(nowe_zmienne) is False:                            #testujemy nowa waluacje
                return False

        return True


class Koniunkcja(Formula):
    def oblicz(self, p, q):
       if p is True and q is True:
           return True
       else:
           return False

    def __str__(self, p, q):
        return " and(" + str(p) + " " + str(q) + ")"


class Alternatywa(Formula):
    def oblicz(self, p, q):
       if p is True or q is True:
           return True
       else:
           return False

    def __str__(self, p, q):
        return " or(" + str(p) + " " + str(q) + ")"


class Implikacja(Formula):
    def oblicz(self, p, q):
       if p is True and q is False:
           return False
       else:
           return True

    def __str__(self, p, q):
        return " imp(" + str(p) + " " + str(q) + ")"


class Rownowaznosc(Formula):
    def oblicz(self, p, q):
       if p is q:
           return True
       else:
           return False

    def __str__(self, p, q):
        return " wtw(" + str(p) + " " + str(q) + ")"


class Negacja(Formula):
    def oblicz(self, p):
        if p is True:
            return False
        else:
            return True

    def __str__(self, p):
        return " not(" + str(p) + ")"


#tworzymy testy

formula1 = Formula((True, 'p'), (False, 'q'), ('or', 'or'), (False, False), (True, 'p'), ('imp', 'imp'), ('and', 'and'))
print(formula1.__str__())
print(formula1.oblicz(formula1.zmienne))
print(formula1.tautologia())

formula2 = Formula((False, 'p'), ('not', 'not'))
print(formula2.__str__())
print(formula2.oblicz(formula2.zmienne))
print(formula2.tautologia())

formula3 = Formula((False, 'p'), ('not', 'not'), (False, 'p'), ('not', 'not'), (False, 'p'), ('imp', 'imp'),
                   ('imp', 'imp'))                          #"reductio ad absurdum" - tautologia
print(formula3.__str__())
print(formula3.oblicz(formula3.zmienne))
print(formula3.tautologia())

formula4 = Formula((True, 'p'), (False, 'q'), ('imp', 'imp'))
print(formula4.__str__())
print(formula4.oblicz(formula4.zmienne))  #tak dziala implikacja na potrzeby ONP (mozna zrobic odwrotnie)

formula5 = Formula((True, 'p'), (False, 'q'), ('and', 'and'), ('not', 'not'), (True, 'p'), ('not', 'not'), (False, 'q'),
                   ('not', 'not'), ('or', 'or'), ('wtw', 'wtw'))         #prawo De Morgana
print(formula5.__str__())
print(formula5.oblicz(formula5.zmienne))
print(formula5.tautologia())