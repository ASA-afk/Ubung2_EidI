## Aufgabe 2.a ##
text=input("Text der verschlüsselt werden soll: ")
code_Verschiebung=int(input("Eine Zahl grösser als null: "))
code=""

if code_Verschiebung > 0:
    for z in text:
        code+=chr((ord(z) + code_Verschiebung)%128)
else:
    print("Keine negative Zahl erlaubt!")
print(code)