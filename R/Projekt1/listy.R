#tworzenie listy - funckaj list()
l <- list(4:8, "uwm", c(T, F, F, T), sample(1:70, 7))
l
#nazywanie elementow listy

ln <- list(ala = 4:8, x1 = 'uwm', logi = c(T, F, F, T), s = sample(1:70, 7))
ln

#str - struktura liusty

str(l)

str(ln)

#names - wyrzuca nazwy z listy

names(l)
names(ln)

#zagniezdzanie listy w liscie
lll <- list(1:6, list("uwm", c(T, T, T, F), 245))
lll
str(lll)

# liste mozna tworzyc przy pomcy funcji c
#funkcja sama wie, ze ma to przeksztacić na liste
#ale nie tworzy listy list tylko rozbija elementy na 
#x elementow listy
l3 <- c(list("ala", 6), c(4, 7, 1), list("A", "B"))
l3
l4 <- list(list("ala", 6), c(4, 7, 1), list("A", "B"))
l4

str(l3)
str(l4)

#adresacja:
#wybieranie elemtnow listy przy pomocy [] - lista elemtntow
#, [[]] - element poprzez indeks, $ poprzez nazwe

li <- list(pff = c(3,6,2), zz= 1:9, ch = c('df', 'dsa'), rl = list(4:7, 2:9))
li

str(li)
li[3]

li[c(3,1)]
r <- li[c(3,1)]
r

r <- li[-c(3,1)]
r

li
str(li[c(T, F, F, T)])

li
li[[2]]
str(li[[2]])
str(li[[4]])

li
li$pff
li$zz
li$rl

#elementow z elementow

li[1] #tutaj dostaje element listy
li[[1]] #tutaj dostaje wektor
li[[1]][1] #laczenie adresacji dostaje 1 element wektora

v <- li[[3]]
v
v[1]

li
li[[1]]
li[[2]]
li[[c(1,2)]]  #pierwszy elemt z 1 elemetu

li$zz
li$zz[c(-3,-5)]

li$rl
li$rl[2]
li$rl[2][6]

#przypisywanie wartosci do elementow listy dziala jak z wektorami
li[1] <- letters
li[1]
li$pff <- letters
li


li
li[[4]]
li[[4]][[2]]
li[[4]][[2]][5]

li$gg <- list(z1 = c(2,3), z2 = c(5,6))
li
