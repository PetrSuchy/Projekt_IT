class Pojisteny:
    def __init__ (self, jmeno, prijmeni, cislo, vek):
        self.jmeno = jmeno
        self.prijmeni = prijmeni
        self.cislo = cislo
        self.vek = vek

    def __str__ (self):
        return str(self.jmeno) + " " +  str(self.prijmeni) + " " + str(self.cislo) + " " + str(self.vek)
