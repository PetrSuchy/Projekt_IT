from pojisteny import Pojisteny


class Seznam:

    seznam = None

    def __init__(self):
       self.seznam = []

    def pridat_pojisteny (self):

        jmeno = input("Zadejte jméno   ")
        prijmeni = input("Zadejte příjmení   ")
        cislo = input("Zadejte telefonní číslo   ")
        vek = input("Zadejte věk  ")

        self.seznam.append(Pojisteny(jmeno, prijmeni, cislo, vek))
        print(self.seznam)
        
