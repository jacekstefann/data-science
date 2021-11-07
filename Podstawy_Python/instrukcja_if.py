# if warunek:
    # kod do wykonania jeżeli powyższy warunek jest spełniony

liczba = 1

if liczba < 10:
    print('To dość mała liczba')
elif 9 < liczba < 100:  # to jest wersja skrócona warunku
    print('To już całkiem duża liczba')
else:
    print('To musi być wielka liczba')


# warunek w elif mozna rozpisac na 2 sposoby
# wersja skrocona:
# elif 9 < liczba < 100:  

# pelna:
# elif liczba > 9 and liczba < 100:  


# input - funkcja, ktora czeka na wprowadzeie wartosci z klawiatury
#  input zawsze zwraca string

# w instrukcji warunkowej if mozna stosowac np. in (not in) itp


#  pod zmienna name jest przechowywana nazwa uchuchomienoego pliku
# jak uruchamian kod w interpreterze to kod sie wykona bo name  = main
#  a jak kod bedzie zaimportowany to moze sie nie wykonac jezeli taki warunek zostanie wprowadzony
if __name__ == '__main__':
    pass


import sys
# read line zachowuje tez np. przejscie do nowej linii \n czego juz nie przechowuje 
# print
wejscie = sys.stdin.readline()
sys.stdout.write("dasdasdasda")


