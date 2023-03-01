from pojisteny import Pojisteny

from seznam import Seznam


def main():
    s = Seznam()
    seznam = s.seznam
    pokracovat = True
    while (pokracovat):

        print("------------------------------")
        print("Evidence pojištěných")
        print("------------------------------")
        print("Vyberte si akci:")
        print("1 - Přidat nového pojištěného")
        print("2 - Vypsat všechny pojištěné")
        print("3 - Vyhledat pojištěného")
        print("4 - Konec")

        cislo = input()

        if cislo == "1":
            print ("Přidat nového pojištěného")
            s.pridat_pojisteny()
            print ("Data byla uložena. Pokračujte libovolnou klávesou...")

        elif cislo == "2":
            print ("Vypsat všechny pojištěné") 
            for pojisteny in seznam:
                print(pojisteny)
                print ("Pokračujte libovolnou klávesou...")
                
        elif cislo == "3":
            print ("Vyhledat pojištěného")
            hledaneJmeno = input("Zadejte hledané jméno: ")
            hledanePrijmeni = input("Zadejte hledané příjmení: ")
            for pojisteny in seznam:
                if(hledaneJmeno == pojisteny.jmeno and hledanePrijmeni == pojisteny.prijmeni):
                    print(pojisteny)
                    print ("Pokračujte libovolnou klávesou...")
                  
        elif cislo == "4":
            print ("Konec")
            pokracovat = False
            print ("Pokračujte libovolnou klávesou...")
        else:
            print("Nesprávné zadání. Zadejte novou volbu!")
   

if __name__ == "__main__":
   print()
   main()
