#1
v1 <- c(-2,-1,0,1,2,3,4)
v2 <- c(-2:4)
v3 <- c(seq(from=-2, to=4))

v1;v2;v3

identical(v1,v2,v3)


d <- c(v1, 3:1, rep(seq(8.1,9.3,0.3),times=2), 1:-4)

mean(d)

length(d)

d1 <- d + v1
d1

d2 <- c(d1, v2)
d2

v <- rep(d, times=3)
v

z <- rep(d, each=2)
z

typeof(d)

f <- c(5:9)

v3+f

#14
d <- d + c(3,5)
1:28
nieparzyste = seq(1,28,by=2)
parzyste = seq(2,28,by=2)
d[nieparzyste]

d[nieparzyste] <- d[nieparzyste] +5
d[parzyste] <- d[parzyste] + 3

d[c(T,F)]
d[c(T,F)] <- d[c(T,F)] + 5
d[c(F,T)] <- d[c(F,T)] + 3



#15
d <- d + c(0,0,15)

#16
l <- letters[1:13]
l

#17
l[1:3]

#18
l[c(F,T)]

l(seq(2, length(l), by=2))

#19
l[l>"g"]

#20
q <- seq(-5,5, length.out = 20)
q

q <- sample(-5:5, 20, replace = T)
q

#21
q>2

#22
lq <- q>2
q[lq]

#23
length(q[q>2])

#alternatywa
sum(lq)

#24
q[c(F,F,T)]

#25
q[q*q>7]

#26
a1 <- 4:7
a2 <- 0:9

#27
sum(a1)

#28
d[order(d)]





