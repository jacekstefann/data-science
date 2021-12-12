#instrukcja warunkowa if

x <- rnorm(10)
sum(x)

if(sum(x) >3) {
  print("wieksze od 3")
} else {
  print("mniejsze od 3")
}

if(sum(x) >3) {
  print("wieksze od 3")
}

#petle
#petla przechodzi i wykonuje sie dla wszystkich elemtnow wekrotra
for(i in c(3,1,2,4)){
  print(i)
}

#while
#wykonuje sie do momemntu kiedy warunek jest true
x <- 5
while (x>3){
  print(x)
  x <- x-1
}

# break koniec natychmiastowy petli
# next nastepna iteracja

x <- sample(1:8,8)
for(i in x){
  print(i)
  if(i==4){
    print("koniec")
    break
  }
}

#petla nieskonczona repeat - robi tak dlugo az dojdzie do break
#petla bez warunkow rob dopuki cos
x<-10
repeat {
  x <- x-1
  if(x>4) next
  print(x)
  if(x<0) break
}



#zad 1
v <- sample(-100:100,10)
v
#zad 2
if(mean(v)>20){
  print("TAK")
} else {
  print("NIE")
}
# zad 3
a <- 0
for(i in v){
  a <- a + i
}
a
