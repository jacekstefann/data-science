#1
t <- sample(20:90, 100, replace = T)

#2
t[t>60 & t < 80] = NA
t

#3
is.na(t)

#4
v <- sample(-7:3, 20, replace = T)

#5
sqrt(v)

#6
v[is.nan(sqrt(v))]

#7
vnii <- c(sqrt(-1), exp(1000), -exp(1000))

#8
vnii[is.infinite(vnii)]=42
vnii
