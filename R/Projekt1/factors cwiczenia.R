#1
v <- c("maly", "sredni", "duzy")
d <- sample(v,17, replace = T)
vf1 <- factor(d)
vf1

#2
ff1 <- factor(vf1)
ff1

#3
vf2 <- sample(1:6, 14, replace = T)

#4
ff2 <- factor(vf2, levels=1:6, lebels = LETTERS[6:1])
ff2

#5
levels(ff2)

#6
sum(ff2=="c")

#7
ordered(vf2)
factor(vf2, ordered = T)

#8
table(vf2)

#9
ff2[c(1,5,12)]

#10
length(ff2[ff2=="A" | ff2=="D"])
