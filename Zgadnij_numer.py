#Komputer losuje numer, a użytkownik wpisuje swoje propozycje – komputer ocenia,
#czy podana wartość jest większa czy mniejsza od wylosowanej.Liczby możesz
#odgadywać do skutku.

import random
from random import randint
import time


def dashboard():
    print('''1 - [G]raj
2 - [Z]asady gry
3 - [R]ekordy
4 - [U]stawienia
5 - [P]omoc
6 - [K]oniec
''')
    
    
def instruction():
    print('''Komputer losuje numer, a użytkownik wpisuje swoje propozycje,
komputer ocenia, czy podana wartość jest większa czy mniejsza od wylosowanej.
Liczby możesz odgadywać do skutku.''')


def win(com, user):
    if number == choice:
        print('Gratulacje! Trafiles/as te liczbe. Ta liczba to: ', number)
        return False
    elif com > user and (user > start - 1 and user < end + 1):
        print('Komputer wybral wieksza liczbe')
        return True
    elif com < number and (user > start - 1 and user < end + 1):
        print('Komputer wybral mniejsza liczbe')
        return True
    elif user < start:
        print('Blad! Liczba spoza zakresu! Wybierz wieksza liczbe')
        return True
    elif user > end:
        print('Blad! Liczba spoza zakresu! Wybierz mniejsza liczbe')
        return True
    
    
def summary(player_att, gt1, gt2):
    print()
    print('Podsumowanie Twojej gry:')
    print('Zakres gry: ', gt1, '-', gt2, sep = '')
    print('Twoja liczba prob wyniosla: ', player_att, sep = '')
    print()

    
def game():
    global start
    global end
    attempts = 0    
    print()
    print('Wybierz zakres z jakiej puli komputer ma wylosowac liczbe')
    print()
    start = int(input('Podaj poczatek puli: '))
    end = int(input('Podaj koniec puli: '))
    print('Trwa wybieranie liczby z zakresu ', start, ' i ', end, '...', sep = '')
    print()
    time.sleep(3)
    global choice
    choice = randint(start, end)
    
    
    new = True


    while new:
        global number
        number = int(input('Podaj swoja liczbe: '))
        print()
        attempts += 1
        if win(choice, number) == False:
            summary(attempts, start, end) 
            while True:
                answer = input('Czy chcesz zagrac jeszcze raz? (Y/N): ')
                print()
                if answer.lower() == 'y':
                    new = True
                    attempts = 0
                    print('Wybierz zakres z jakiej puli komputer ma wylosowac liczbe')
                    print()
                    start = int(input('Podaj poczatek puli: '))
                    end = int(input('Podaj koniec puli: '))
                    print('Trwa wybieranie liczby z zakresu: ', start, ' i ', end)
                    print()
                    time.sleep(3)
                    choice = randint(start, end)
                    break
                elif answer.lower() == 'n':
                    print('KONIEC')
                    new = False
                    break
                else:
                    print('Ups... Cos poszlo nie tak, sprobuj jeszcze raz')
                    continue

                    
while True:
    dashboard()
    menu = input('Co chcesz zrobic? ')
    print()
    if menu.lower() == 'g':
        game()
        print()
        continue
    elif menu.lower() == 'z':
        instruction()
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

