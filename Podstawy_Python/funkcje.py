# definicja funkcji
# def nazwa_funckji(arg_pozycyjny, arg_domyslny=wartosc, *arg4):

# pass - nic nie robi

def poteguj(liczba=1, potega=2):
    pass

# poteguj() - wywoluje funckje bez arugmentow bo sa domyslne

# poteguj(3,2) - mozna tez wywolac funckje z wartosciami

# poteguj(3) - mozna tez wywolac funckje z wartosciami
# poteguj(liczba=3,potega=2) - mozna tez wywolac funckje z wartosciami przypisanymi

def licz(*liczby):
    return sum(liczby)

print(licz(1,3,4))


# kwargs 

def drukuj(**kwargs):
    print(kwargs)

drukuj(imie= 'Adam', nazwisko = 'Mick')

# retrun - okresla czy funckaj cos zwraca
# funkcja nie musi miec wyrazenia return

# bez return funkcja nic nie zwraca i ma to typ Nonetype

# funckja do okreslania co cos zwraca
def co_zwracasz(a,b):
    return a*b, a**b

# powyższa funckja zwraca krotke - tuple

# pierwsze wywolanie return konczy dzialanie funckji !!!!





