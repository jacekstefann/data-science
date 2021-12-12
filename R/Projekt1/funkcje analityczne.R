#rozklady przedrostek r
#rozklad jednorodny
runif(10)
runif(10,5,10)

#rozklad normalny
rnorm(10)

#funckje rozkladu przedrostek d
dnorm(-5:3)
pnorm(0,5)
qnorm(0.6, mean=0, sd=1)

#mean - srednia
#median
#quantile

p <- runif(7, 0, 10)
p
mean(p)
median(p)
quantile(p)

p1 <- c(p, NA)
p1
mean(p1)
#pomijamy wartosci NA ta opcja jest we wszystkich funkkcjach analitycznych
mean(p1, na.rm = T)

quantile(p)["25%"]

sd(p)
var(p)
min(p)
max(p)


#min i max miedzy elementami wektorow
x <- sample(1:9 ,5)
y <- sample(1:9 ,5)

x;y
pmin(x, y)
pmax(x,y)
range(p)

#podsumiwanie zbioru
summary(sample(1:90, 25))

summary(c(T,T,T,F,F,F))
        
#zad 1
v <- rnorm(30)

#zad 2
mean(v)
#zad 3
median(v)
#zad 4
quantile(v,0.1)
#zad 5
sd(v)
#zad 6
p1 <- sample(-10:10,7)
p1
#zad 7
p2 <- c(-3:4)
p2
#zad 8
min(p1)
#zad 9
range(v)
#zad 10
a <- pmin(p1,p2)
a
