
#tworzenie macierzy
matrix(data = 11:20, nrow=2, ncol=5)

matrix(data = 11:20, nrow=2, ncol=5, byrow = T)

matrix(data = 11:20, nrow=5, ncol=5, byrow = T)

matrix(c(3,7,2,9,3), nrow=5, ncol = 3)

matrix(c(3,7,2,9,3), nrow=7, ncol = 3)

#dim - wyswietla i nadaje wymiary

m1 <- matrix(data = 11:20, nrow=2, ncol=5)

dim(m1)

m <- 1:20

is.matrix(m)

is.matrix(m1)

dim(m)

dim(m) <- c(4,5)

dim(m)
m <- 1:20
m
dim(m)

dim(m) <- c(20,5)
dim(m) <- c(2,3)

m1

length(m1)

nrow(m1)

ncol(m1)

rownames(m1)

rownames(m1) <- c("pierwszy", "drugi")

colnames(m1) <- c("a", "b", 
           "c", "d", "e")

m1

#rbind() do istniejacej macierzy dolaczamy kolejna poprzez inna 

rbind(c(2,3,6,5), c(6,7,5,4))

rbind(c(2,3,6,5), c(6,7,5,4), c(1,2,3,4,5,6))

#cbind laczenie po kolumnach
cbind(1:5, c(4,3), 3)

m1 <- matrix(1:6, nrow=2)
m2 <- matrix(c(87,32), nrow=2)
m1;  m2

rbind(m1,m2)
# nie da sie tego powyzej bo liczba wierszy sie niezgadza

cbind(m1,m2)

#adresacja  - dostep do elementow przez nr wierszy i kolumny, jak tego nie ma to biore wszystko
# -x jak jest - to tych elementow nie bierzemy

m1

#wybieram 2 wiersz 3ci element
m1[2,3]

#po za zakrem
m1[1,5]

#nie biore 3ciej kolumny
m1[1,-2]

#biore tylko 1 wiersz
m1[1,]

c(T,F)

#jak nie wskazuje wymiaru mamy indeksowanie jak w wektorach
m1[c(T,F)]
m1[c(T,F),]
m1[c(T,T,F),]
m1[c(T,T,F)]

