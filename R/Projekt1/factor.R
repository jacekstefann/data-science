# tworzenie factora poprzez funcke fac 
#
#
#

v1 <- c("a", "b", "c", "a", "e", "a", "a")
f1 <- factor(v1)
f1 
f2 <- factor(v1, levels = c("c", "b", "a"))
f2
f3 <- factor(v1, levels = c("c", "b", "a", "d"))
f3
f4 <- factor(v1, levels = c("c", "b", "a", "d"), labels = c("ciocia", "basia", "ania", "danuta"))
f4


ff <- factor(c(1,4,5,2,2,5,3,2,1)
             , levels = 1:5
             , labels = c("jeden", "dwa", "trzy", "cztery", "piec"))

ff
levels(ff) <- c("j", "d", "t", "c", "p")
ff

levels(ff)
levels(ff) <- c("malo", "malo", "srednio", "duzo", "duzo")
ff

#zmiana levels,wartosci jest nieodwracalna

#faktor z kolejnoscia
f01 <- ordered(c(1,2,3,3,3,2,2,1)
               , levels = 3:1
               , labels = c("zle", "srednio", "dobrze"))
f01
f02 <- factor(c(1,2,3,3,3,2,2,1)
               , levels = c(3,2,1)
               , labels = c("zle", "srednio", "dobrze")
               , ordered = T)
f02
f03 <- ordered(c("A", "B", "F")
             , levels = c("A", "B", "C", "D", "E", "F"))
f03
levels(f03) <- c(5,4,3,2,1)

vv <- sample(1:5, 10, replace = T)
vv
fv <- factanal(vv, levels = 1:10)
fv <- factor(vv, levels=1:10)
fo <- factor(vv, levels=10:1)
fo
fv #ile wartosci mamy w faktorze
table(vv)
table(fv)
table(fo)

as.numeric(ff)
ff
as.character(ff) #teraz nie dostajemy faktorow tylko wektor znakowy

#jak sie dostac do wartosci faktorow
ff
#1 element
ff[1]
#2, 4, 1 element
ff[c(2,4,1)]
#biore co drugi elemtn
ff[c(T,F)]
ff == "malo"
ff[ff=="malo"]
ff[ff=="malo" | ff == "duzo"]
