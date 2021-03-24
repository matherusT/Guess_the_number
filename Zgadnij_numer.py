#Komputer losuje numer, a użytkownik wpisuje swoje propozycje – komputer ocenia,
#czy podana wartość jest większa czy mniejsza od wylosowanej.Liczby możesz
#odgadywać do skutku.

import random
from random import randint
import time

def panel():
    print('''1 - [G]raj
2 - [Z]asady gry
3 - [R]ekordy
4 - [U]stawienia
5 - [P]omoc
6 - [K]oniec
''')
    
def instrukcja():
    print('''Komputer losuje numer, a użytkownik wpisuje swoje propozycje,
komputer ocenia, czy podana wartość jest większa czy mniejsza od wylosowanej.
Liczby możesz odgadywać do skutku.''')

def panel():
    
    print('''1 - [G]raj
2 - [Z]asady gry
3 - [R]ekordy
4 - [U]stawienia
5 - [P]omoc

''')
    
def czy_wygrana(kom, user):
    if liczba == wybor:
        print('Gratulacje! Trafiles/as te liczbe. Ta liczba to: ', liczba)
        return False
    elif kom > user and (user > start - 1 and user < end + 1):
        print('Komputer wybral wieksza liczbe')
        return True
    elif kom < liczba and (user > start - 1 and user < end + 1):
        print('Komputer wybral mniejsza liczbe')
        return True
    elif user < start:
        print('Blad! Liczba spoza zakresu! Wybierz wieksza liczbe')
        return True
    elif user > end:
        print('Blad! Liczba spoza zakresu! Wybierz mniejsza liczbe')
        return True
    
def podsumowanie(proby_gracza, gt1, gt2):
    print()
    print('Podsumowanie Twojej gry:')
    print('Zakres gry: ', gt1, '-', gt2, sep = '')
    print('Twoja liczba prob wyniosla: ', proby_gracza, sep = '')
    print()

def gra():
    global start
    global end
    proby = 0    
    print()
    print('Wybierz zakres z jakiej puli komputer ma wylosowac liczbe')
    print()
    start = int(input('Podaj poczatek puli: '))
    end = int(input('Podaj koniec puli: '))
    print('Trwa wybieranie liczby z zakresu ', start, ' i ', end, '...', sep = '')
    print()
    time.sleep(3)
    global wybor
    wybor = randint(start, end)
    
    nowa = True


    while nowa:
        global liczba
        liczba = int(input('Podaj swoja liczbe: '))
        print()
        proby += 1
        if czy_wygrana(wybor, liczba) == False:
            podsumowanie(proby, start, end) 
            while True:
                odp = input('Czy chcesz zagrac jeszcze raz? (Y/N): ')
                print()
                if odp.lower() == 'y':
                    nowa = True
                    proby = 0
                    print('Wybierz zakres z jakiej puli komputer ma wylosowac liczbe')
                    print()
                    start = int(input('Podaj poczatek puli: '))
                    end = int(input('Podaj koniec puli: '))
                    print('Trwa wybieranie liczby z zakresu: ', start, ' i ', end)
                    print()
                    time.sleep(3)
                    wybor = randint(start, end)
                    break
                elif odp.lower() == 'n':
                    print('KONIEC')
                    nowa = False
                    break
                else:
                    print('Ups... Cos poszlo nie tak, sprobuj jeszcze raz')
                    continue

while True:
    panel()
    menu = input('Co chcesz zrobic? ')
    print()
    if menu.lower() == 'g':
        gra()
        print()
        continue
    elif menu.lower() == 'z':
        instrukcja()
        print()
        continue
    elif menu.lower() == 'r':
        pass
        continue
    elif menu.lower() == 'u':
        pass
        continue
    elif menu.lower() == 'p':
        pass
        continue
    elif menu.lower() == 'k':
        pass
        break
    else:
        print('''Cos poszlo nie tak :(
Sprobuj jeszcze raz ''')
        print()

