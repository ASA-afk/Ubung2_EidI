## aufgabe 2.b.1 ##
text=input("Text der entschlüsselt werden soll: ")
code_Verschiebung=int(input("Eine Zahl grösser als null: "))
code=""

if code_Verschiebung > 0:
    for z in text:
        code+=chr((ord(z) - code_Verschiebung)%128)
else:
    print("Keine negative Zahl erlaubt!")

print(code)


## aufgabe 2.b.2 ##
w=code
d="$".join(w)
print(d)
        

## aufgabe 2.b.3 ##
half=len(w)//2

if len(w)%2==0:
    B=w[half::1]
    A=w[:half:1]
    print(B+A)
else:
    B=w[half::1]
    A=w[:half:1]
    print(B+A)