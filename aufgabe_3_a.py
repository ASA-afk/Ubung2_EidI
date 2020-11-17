## aufgabe 3.a ##

b=input("Eine Binärzahl nur mit 0 und 1 eingeben: ")
b=b[::-1]
dezimal=0
for binary in range(len(b)):
    if len(b)==0:
        print("Es wurde keine Binärzahl eingegeben.")

    elif b[binary] == "1":
        dezimal+=2**binary

    elif b[binary]=="0":
        dezimal+=0

    else:
        print("Ungültige Eingabe!")


print("Die Dezimalzahl lautet:",dezimal)