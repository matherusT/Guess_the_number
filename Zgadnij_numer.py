#Komputer losuje numer, a użytkownik wpisuje swoje propozycje – komputer ocenia,
#czy podana wartość jest większa czy mniejsza od wylosowanej.Liczby możesz
#odgadywać do skutku.

import random
from random import randint
import time

def instrukcja():
    print('''Komputer losuje numer, a użytkownik wpisuje swoje propozycje
– komputer ocenia, czy podana wartość jest większa czy mniejsza od wylosowanej.
Liczby możesz odgadywać do skutku.''')


def czy_wygrana(wybor, liczba):
    if liczba == wybor:
        print('Gratulacje! Trafiles/as te liczbe. Ta liczba to: ', liczba)
        return False
    elif wybor > liczba:
        print('Komputer wybral wieksza liczbe')
        return True
    elif wybor < liczba:
        print('Komputer wybral mniejsza liczbe')
        return True
    else:
        print('Liczba spoza zakresu')
        return True
    
instrukcja()
print('Wybierz zakres z jakiej puli komputer ma wylosowac liczbe')
start = int(input('Podaj poczatek puli: '))
end = int(input('Podaj koniec puli: '))
print('Trwa wybieranie liczby z zakresu: ', start, ' i ', end)
time.sleep(3)
wybor = randint(start, end)

while czy_wygrana:
    liczba = int(input('Podaj swoja liczbe: '))
    czy_wygrana(wybor, liczba)

    

