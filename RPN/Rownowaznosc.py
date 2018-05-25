class Rownowaznosc():
    def __init__(self, p, q):
        self.zmienne = p[0], q[0]
        self.p = p[1]
        self.q = q[1]

    def oblicz(self, zmienne):
       if zmienne[0] == zmienne[1]:
           return True
       else:
           return False

    def __str__(self, zdanie):
        if zdanie == 'False':
            return 'False'
        elif zdanie == 'True':
            return 'True'
        else:
            return zdanie

    def wypisz(self):
        print(str(self.p) + ' wtw ' + str(self.q))