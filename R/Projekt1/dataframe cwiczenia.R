#1
C1 = c("Ala", "Beata", "Marek", "Igor", "Franek", "Adam"
       , "Tomek", "Argh")
C1

S1 = c("k", "k", "m", "m", "m", "m", "m", "m")
S1

Hi = sample(100:220,8)
Hi

df = data.frame(C1, S1, Hi)

df

#2
str(df)

#3
df

#4
dim(df)

#5
df[c(2,5),]

#6
df$Hi

#7
names(df)
colnames(df)

#8
df$Hi>150
df[df$Hi>150,]

subset(df, subset = Hi > 150)

