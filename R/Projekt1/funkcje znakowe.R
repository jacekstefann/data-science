na <- c("Ala ma kota", "napis", 
        "UWM jest ok")
nchar(na)
# liczba znakow dziala to lub length()
length(na)
tolower(na)
toupper(na)
#laczenie stringow - paste bazowo daje spacje miedzy stringami
paste("Ala", 'ma kota')

p <- c(3,56,12,553,11)
paste("Element cztery to:", p[4])

p
paste("osoba",p)
paste("osoba",p, sep="_")
paste(c("osoba", "zwierz"),p, sep="_")
paste("osoba",p, sep=" ma ")
#collapse laczy w 1 napis okreslamy czym laczymy
paste(c("ala", "ma", "kly"), collapse = " ")

#wycinanie
substring("Ala ma kota", first = 5)
substring("Ala ma kota", first = 5, last = 10)
substring("Ala ma kota", 5, 7)

#dla substr trzeba zawsze podac start i koniec
# dla substring nie trzeba
substr("Ala ma kota", 5, 7)
ss <- c("Ala ma kota", "Nap"
        , "jezyk r wprowadzenie")

substring(ss,2,5) 

substring(ss,2,5) <- "1234"
ss
#podmieniane sa tylko tyle znakow ile wycinamy nawet jak przypisywany napis jest dluzszy
substring(ss,2,5) <- "123423123"
substring(ss,2,5) <- "9"

#strsplit rozbija na czesci wynikiem jest lista

s <- strsplit("Kaja ma kajak", " ")
s
#rozbicie na pojedyncze znaki
strsplit("Kaja ma kajak", "")

unlist(s) # <-- do zaliczenia
s 
r <- strsplit("Kaja ma kajak" ,"j")
r
r <- strsplit(c("Kaja", "ma", "kajak"), "j")

r
unlist(r)

#sub zmienia nam pierwsze wystapienia w napisie
#gsub zmienia wszystkie wystapienia
s <- "sa samochody szybkie i sa samochody zielone"
sub(x=s, pattern = "samochody", replacement = 
      " rowery")
s <- "sa samochody szybkie i sa samochody zielone"
gsub(x=s, pattern = "samochody", replacement = 
      " rowery")
gsub("sa", "mam", s)
#sa case sensitive
#zeby to ominac
gsub("sa", "mam", s, ignore.case = TRUE)

m <- c("ala", "be", "ce", "de", "d")
"ce" %in% m
c("ce", "zong") %in% m
match("ce", m)
grep("ola", m)
grep("[0-9", m)
grep("a$", m)
m[grep("a$", m)]

#zad 1
s <- c("DUŻE", "male", "te inne 123456789")
#zad2
length(s)
#zad 3
s1 <- paste(s,collapse = " ")
s1
#zad 4
tolower(s1)
#zad 5
# t <- sample(20:90, 100
t <- seq(0,300)
t
b <- paste("a", t, sep = ".")
b
#zad 6
grep("a.9$", b)

#zad7
c <- "Ala ma kota. Ala ma rybki"
z <- sub(x=c, pattern = "kota", replacement = 
      " psa")
z
