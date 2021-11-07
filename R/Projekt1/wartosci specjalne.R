#Na - wartosc niedostepna sprawdzenie: is.na()

v <- c(44,11,NA)
v
v[3]

is.na(v[3])

as.numeric(v)

is.na(v)

#wartosci, ktore nie sa na
v[!is.na(v)]
#wartosci, ktore sa na
v[is.na(v)]
23/0

#kolejna wartoscia specjalna jest null
#sprawdzenie is.null()


c <- c(1,2,34, NULL)
c
#null nie dopisuje sie do werktora ale mozna ja przypisac do zmiennej

d <- NULL
d

is.null(d)

#kolejne zmienne specjalne to inf -inf - nieskonczonosc
23/0

is.infinite(23/0)

2/5
#sprawdzamy czy wartosc jest skonczona
is.finite(2/5)


