# Zadanie 1
# Stwórz słownik gdzie kluczami będą numery miesięcy (rozpoczynając od 1) 
# a wartościami nazwy polskich miesięcy.

# Zadanie 2
# Stwórz podobny słownik jak w zadaniu 1, ale z angielskimi nazwami miesięcy. 
# Połącz teraz słowniki tak, żeby przykładowo dla kwietnia, dostać się 
# poprzez wyrażenie: months['pl'][4].

# Zadanie 3
# Wykorzystując ciąg tekstowy 'Marianna' oraz metodę fromkeys() dla słowników stwórz słownik, 
# który będzie zawierał jako klucze unikalne litery w/w imienia a jako wartość każdy klucz będzie 
# miał przypisaną wartość 1. Poprawne wyjście: {'M': 1, 'a': 1, 'r': 1, 'i': 1, 'n': 1}

# zad 1
miesiace_pl = {1: 'styczen'
                , 2: 'luty'
                , 3: 'marzec'
                , 4: 'kwiecien'
                , 5: 'maj'
                , 6: 'czerwiec'
                , 7: 'lipiec'
                , 8: 'sierpien'
                , 9: 'wrzesien'
                , 10: 'pazdziernik'
                , 11: 'listopad'
                , 12: 'grudzein'}


# zad 2
miesiace_eng = {1: 'januyary'
                , 2: 'february'
                , 3: 'march'
                , 4: 'april'
                , 5: 'may'
                , 6: 'june'
                , 7: 'july'
                , 8: 'august'
                , 9: 'september'
                , 10: 'october'
                , 11: 'november'
                , 12: 'december'}

months = {"pl": miesiace_pl
        , "eng": miesiace_eng}

print(months["pl"][4])

# zad 3

slowo = 'Marianna'
test = dict.fromkeys(slowo, 1)
print(test)

