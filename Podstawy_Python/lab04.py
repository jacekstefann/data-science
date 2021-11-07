# Zadanie 1
# Napisz skrypt, który pobiera od użytkownika zdanie i liczy w nim spacje. 
# Wynik wyświetla na ekranie (użyj instrukcji input).


# Zadanie 3
# Napisz skrypt, który pobiera od użytkownika trzy liczby a, b i c. Sprawdza następujące warunki:

# czy a zawiera się w przedziale (0,10>
# oraz czy jednocześnie a>b lub b>c.
# Jeśli warunki są spełnione lub nie to ma się wyświetlić odpowiedni komunikat na ekranie.

# zad 1
zdanie = input("Podaj zdanie: ")
spacje = zdanie.count(" ")

print('Podane zdanie: "{a}" ma {b} spacji.'.format(a=zdanie, b=spacje))

# zad 3
print("Podaj proszę następujące liczby: ")
a = input("Podaj liczbę a: ")
b = input("Podaj liczbę b: ")
c = input("Podaj liczbę c: ")

if a.isalnum() and b.isalnum() and c.isalnum():
    if 0 < int(a) < 10:
        print("A zawiera się w przedziale <0,10>")
    if int(a) > int(b) or int(b) > int(c):
        print("A spełnia drugi warunek")