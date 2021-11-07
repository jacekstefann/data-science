#tworzenie dataframe (dwa sposby)
f <- c("audi", "fiat", "opel", "mazda", "tata")
t <- c("sedan", "combi", "sedan", "sedan", "combi")
l <- c(3800, 5000, 3640, 2000, 1900)
df1 <- data.frame(f,t,l)
df1


df2 <- data.frame(1:5, 5:9, c("a", "c", "f", "c", "z")
                  , c(T,T,T,F,F))
df2
str(df1) #odpytanie struktury
df3 <- data.frame(f,t,l, stringsAsFactors = F)  #aby nie przeksztacac tego w factor
df3
str(df3)

dim(df1)
nrow(df1)
ncol(df1)
head(df1, n=1)

tail(df1)
tail(df1, n=2)
colnames(df1)

#adresacja
df1
#pierwszy element
df1[1] 
#pierwszy i trzeci
df1[c(1,3)]

#pierwszy i trzeci z 1 kolumny
df1[c(1,3),1]
rownames(df1) <- c("j", "d", "t", "c", "p")
df1

df1[,-2]

df1[c(T,F,F,T,T),]
df1[c(T,F,F,T,T)] #bez przecinka bedzie blad bo jest za malo kolumn

df1$f
df1$l
df1$l[1]
df1$l>3000
df1$f[df1$l>3000]
df1[df1$l>3000,]


#prosterze odpytania dfa
df1
subset(df1, subset = l < 3000, select = c(f, l))

#do odpytywania mozna tez uzyc pakietu dplyr
library("dplyr")       

df1 %>% filter(l<3000)



