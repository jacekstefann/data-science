#1
m1 <- matrix(1:24, nrow = 3, ncol = 8)
m1

#2
m2 <- matrix(1:24, ncol = 4)
m2

#3
v <- 1:10
v
dim(v) <- c(2, 5)
v

m3 <- v
m3
is.matrix(m3)


#4
v <- -4:3
v
dim(v) <- c(2,4)
v
m4 <- v
m4
is.matrix(m4)

#5
c <- cbind(m3,m4)

#6
dim(c)
 
#7
a <- c(1:5)
b <- c(5:9)
c <- c(1, 5, 3, 2, 6)

rbind(a, b, c)

#8
v1 <- sample(-3,3, replace = T)
v1
v2 <- sample(-3,3, replace = T)
v2
v3 <- sample(-3,3, replace = T)
v3

#9

cbind(v1, v2, v3)

#10
a <- c(1:20)
a
c <- c(40:59)
c
b <- rep(c(-5, 6), times = 10)
b

mt <- cbind(a, b, c)
mt

cbind(1:20, c(-5,6), 40:59)


#11
mt[c(1,3,length(mt))]


a <- mt[1,1]
b <- mt[3,1]
c <- mt[19,1]

#12
mt[,c(F,T)]

#13
mt[-c(3,17),]

#14
rbind(mt, seq(-600, 300, length.out = 3))
#alternatywa
rbind(mt,sample(-600:300, replace = T))

#15
mt[,mt[4,]>=-10 & mt[4,]<280]
#16
mt[mt>20]
#17
mt[1,2]<-42
#18
mt[,3]<-5
#19
mt[2,]
mt[3,]
mt[2, mt[2,]%%2==0]=2
mt[3, mt[3,]%%2==0]=2
mt
#20
mt[1,]
mt[3,]
mt[3,mt[1,]%%3==0]
#parzyste
mt[3,mt[1,]%%2==0]
