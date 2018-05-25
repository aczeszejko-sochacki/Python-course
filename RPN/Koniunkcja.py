from Formula import Formula

class Koniunkcja(Formula):
    def oblicz(self, p, q):
       if p is True and q is True:
           return True
       else:
           return False

    def __str__(self, p, q):
        return " and(" + str(p) + " " + str(q) + ")"

