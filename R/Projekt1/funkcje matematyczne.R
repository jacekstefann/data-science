#funckje logarytmiczne log(), log10(), log2(), exp()

#log(l, base = 2) logarytm o podstawie 2 moze tez byc log2()

#funkcje trygonometryczne
#sin(), cos(), tan(), sinpi(), cospi()


#round() wartosc do zaokraglenia na - zaokraglaja do dziesiacte, setek itd

s <- seq(100,150, length.out = 8)
s
round(s)
round(s,digits = -1) dziesiatki
round(s,digits = -2) setki
round(s,digits = -3) tysiace

#round zaokragle do najblizszej parzystej
v <- -4.5:4.5
v
round(v)

#floor()
#zaokragla do najblizszej w dol
v <- -2.5:2.5

floor(v)

#ceiling()
#zaokragla w dol do najblizszej
ceiling(v)

#trunc() ucina po przecinku
trunc(v)


