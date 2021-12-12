f1 <- function(p1,p2){
  r <- p1-p2
  return(r)
}
# jak nie ma return to funckja zwraca ostatnie dzialanie (ostatnia linie)

f1(4,2)


#wartosci domyslne:

f1 <- function(p1,p2=1:2){
  r <- p1-p2
  return(r)
}
f1(5)

f1 <- function(p1=1:2,p2){
  r <- p1-p2
  return(r)
}
f1(5)
f1(p2=5)

#zmienne lokalne nie dzialaja wewnatrz funckji
suma <- 21241
f2 <- function(p1){
  suma <- sum(p1)
  return(suma)
}
f2(1:7)

x<-1:4
y<-5:2
x;y
x + y
'+'(x,y)
'+'(x,4)


'%mnozenie%' <- function(x, y){
  return(x*y)
}
2 * 2
2 %mnozenie% 2
'%mnozenie%'(2,2)
#funkcje ze zmiennymi parametrami

'zmien<-' <- function(x, value){
  x <- x*value
  return(x)
}

p <- c(3,5,1,25)
`zmien<-` (p,3)


# zad 1
foo <- function(x){
  return(x)
}

foo(5)
#zad 2
hgtg <- function(){
  return(42)
}
hgtg()

#zad 3
goo <- function(x){
  return(c(-100:100)[x])
}

goo(5)

#zad 4
goo <- function(x){
  if(length(x)!=1){
    warning("Za duzo")
    return(NA)
  }
  
  if(x<1 | x>length(-100:100)){
    warning("za zakresem")
    return(NA)
  }
  
  return(c(-100:100)[x])
}


