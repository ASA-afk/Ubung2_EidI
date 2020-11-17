## aufgabe 3.b ##
dezimal=int(input("Geben sie eine Dezimalzahl ein: "))
binaer=""
if dezimal<0:
    print("Die Zahl ist negativ.")
else:
    while dezimal!=0:
        binaer+=str(dezimal%2)
        dezimal//=2

for b in range(len(binaer)-1,-1,-1):
    print(binaer[b],end='')
print("")


