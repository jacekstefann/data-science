#wywietla datasety, ktore mamy zaladowane w R z pakietow
data()

trees
swiss

#wyswietlenie danych, ktore mamy jeszcze nie zaladowane
data(package = .packages(all.available = TRUE))


veteran 
#zaladowanie niezaladowanych danych z pakietow
data(veteran, package = "survival")

#import eksport danych
vs <- c(132, 5,2,12,512)
fc <- c("R", "c", "RSS")

#save zapisuje zmienna do pliku
#nalezy podawac rozszerzenia bo inaczej zostanie zapisany 
#bez rozszerzenia
save(vs, file = "plik1.RData")
save(vs, fc, file = "plik2.RData")
#ponizsza list to nie lista, tylko lista nazw zmiennych, ktore chcemy zapisac
save(list=c("vs", "fc", "fo"), file = "plik3.RData")


#zapisuje wszystie zmienne do pliku
save.image(file = "wszystko.RData")


#usuwanie obiektow
vs

rm(vs)

vs

#odczyt z pliku (nazwy i typy zmiennych sa zapisywane)
load(file = "plik1.RData")

vs


#obsluga katalogow
dir
dir()

#tylko pliki z okreslonym rozszerzeniem
dir(pattern = "*.Rproj")

getwd()

setwd("D:/")
getwd()

setwd("C:/Users/Jacek/Desktop/data science/data science/R/Projek1")
dir()

getwd()
setwd("C:/Users/Jacek/Desktop/data science/data science/R/Projekt1")


df

#write table - funckja zapisuje csv do pliku
write.table(x=df,file="dane.csv")
write.table(x=df,file="dane.csv", sep=",", na="NULL")
write.table(x=df,file="dane.csv", sep=",", na="NULL"
            , row.names = F)
#write.csv do liczby zmienna przecinkowych uzywa .
#write.csv2 tutaj rozdzielamy liczby zmienno przeciwnkowe przy pomocy ,

#odczyt plikow csv
# read.table
#read.csv
#read.csv2
#dane odczytywane sa w postaci df

rt <- read.csv(file = "dane.csv")
rt

rt <- read.csv2(file = "dane.csv")
rt

rt <- read.table(file = "dane.csv")
rt

#? read.table pomoc do funckji - mozna spradzic opcje

rt <- read.table(file = "dane.csv", sep = ",")
rt

#pliki excela xlsx

#instalacja pakietu do obslugi pliow excel xlsx
install.packages("openxlsx")
#ladowanie pakietu
library(openxlsx)

#zapisu do exela xlsx
#write.xlsx(dane, file = "nazwa pliku")

write.xlsx(df, file = "dane.xlsx")

#paramatryzacja write.xlsx
write.xlsx(df,"dane1.xlsx", sheetName = "off")
write.xlsx(df,"dane1.xlsx", sheetName = "off"
           , row.names = T, overwrite = T
           , keepNa = T)

#odczyt
a <- read.xlsx("dane.xlsx", rowNames = T)
a

#odczyt danych z baz danych
# pakiet rodbc, rjdbc








