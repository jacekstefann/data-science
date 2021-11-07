#  ZBIORY - SETS
klasa = {'Marek', 'Janek', 'Ania', 'Ewa', 'Marek', 'Ania'}

print(klasa)

# a teraz zbiór znaków ze stringa
# set dzieli nam stringa na litery i usuwa duplikaty
czar = set('czabunagunga')
print(czar)

inny_czar = set('abrakadabra')
print(inny_czar)
print(czar - inny_czar) # są w czar, ale nie ma w inny_czar
print(czar.difference(inny_czar)) # to samo, ale inaczej
print(inny_czar - czar) # to nie to samo, jak wiadomo z teorii

print(czar | inny_czar) # znaki w czar lub inny_czar lub obu
print(czar & inny_czar) # przecięcie czyli część wspólna
print(czar.intersection(inny_czar)) # można tak
print(czar ^ inny_czar) # różnica symetryczna

