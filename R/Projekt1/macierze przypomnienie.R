#macierze

m1 <- matrix(sample(1:60,20), nrow = 5, ncol = 4)
m1
m1[4,3]
m1[4,-3]
m1[4,]
m1[,2]
m1[c(4,2), c(-1,-3)] #pobieranie danych z macierzy wektorem chce dane z kolumny 4 i 2, a potem okreslam, ze nie che 1 i 3 elementu
m1
m1[c(T,F)]
m1[c(T,F),]

m1[c(T,T,F),]

m1[c(T,T,F), c(2,4)]

m1[c(T,T,F), c(T,T,F)]

m1[1,, drop=F] # dostaje macierz
m1[1,, drop=T] # dostaje wektor

#wybieranie rzeczy z maciery na podstawie warunkow

m1
m1[5,]
m1[5,]<20
#wyswietlenie wartosci spelaniajcych warunek
m1[5,m1[5,]<20]

kolumny <- m1[5,]<=20
kolumny

m1[5,kolumny]

#zmienaimy wartosc
#zeby cos zmienic trzeba miec najpierw adresacje (wskazac miejsce)

m1
m1[4,2] <- 450
m1
m1[,3] <- 333
m1
m1[2,] <- 222
m1

#elemtenty o okreslonych parametrach (to lub to)
m1[,1]<20 || m1[,1]>40
m1[m1[,1]<20 || m1[,1]>40]

m1[m1[,1]<20 || m1[,1]>40] <- 1000
m1