#1
v <- (-100:100)
l <- c(T,F,T,T,T,F)
c <- c("A", "ja", "jaj", "Oj", "Pff")

#2
save(v, file = "vfile.RData")

#3
save(list = c("l", "c"), file = "lc.RData")

#4
v <- c

v

#5
load(file = "vfile.RData")

v

#6
read.csv(file = "C:/Users/Jacek/Desktop/data science/R/dswp_2021_2022_v03/cwiczenia/pliki/c1.csv"
         )

? read.csv


#7
write.csv(v, file = "vfile.csv")

#8
read.xlsx("C:/Users/Jacek/Desktop/data science/R/dswp_2021_2022_v03/cwiczenia/pliki/x1.xlsx"
          , sheet = 1)

#9
library(foreign)
read.dbf(file = "r.dbf")
