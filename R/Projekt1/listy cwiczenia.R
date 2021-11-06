#1
l1 <- list(a1 = c(sample(1:100,5))
           , a2 = c(T, T, F)
           , a3 = c(sample(letters, 13)))

l1

#2
l1$a3

#3
str(l1)
str(l1$a3)
is.list((l1$a3))

#4
l1[[1]]

#5
l1[[3]][1:3]

#6
names(l1)

#7
mx <- matrix(1:12, nrow = 3, ncol = 4)
mx

l1$moj <- mx

l1

#8
l1[1]

l1$a1[3] 
l1$a1[3] <- 4
l1$a1

#9
l2 <- list(1:43, 3:56, -5:8)
l2

#10
l3 <- c(l1, l2)

l3

#11
l2$ml1 <- l1
l2

#12
l1$moj[2,]
avg <- sum(l1$moj[1,]) / length(l1$moj[1,])
avg
l1$moj[2,] > avg
l1$moj[2,][l1$moj[2,] > avg]
