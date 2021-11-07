# funkcja range()
# odpowiednik seq() w R
# generuje obiekt typu range od do z krokiem
# zawsze musi byc chociaz 1 argument, którmu przypisujemy stop
# bazowo start = 0 i step = 1

liczby = range(5)

# wygenerowanie zakresu 0-5
print(liczby)

print(type(liczby))

# rzutowanie na liste
print(list(liczby))

# roznica: range(100000000000) a list(range(100000000000)) jest taka, że nie tracimy w 1 przypadku
# pamieci komputera, druga opcja nie utworzy sie jezeli komputer nie ma takich zasobow

# range przechowuje dane o poczatku, koncu i mozna po tym iterowac
print(list(range(1,6,2)))

wycinek = slice(1, 6, 2)

imie = 'Marianna'[wycinek]
print(imie)

l = list(range(-11,0,2))
print(l)

# yield - generator

def frange(start, stop, step):
    i = start
    while i < stop:
        #  https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do
        yield i
        i += step


gen = frange(0.1, 0.5, 0.1)
print(gen)
print(type(gen))
print(next(gen))


for i in frange(0.1, 0.5, 0.1):
    print(i)