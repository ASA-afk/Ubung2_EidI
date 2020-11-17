### Carina Moitov
### Florian Ewald
### Arthur Flaum 


## Aufgabe 1.1 ##
o=int(input("Wählen Sie bitte eine Option aus: \n1. Julianischer Kalender \n2. Gregorianischer Kalender \n3. Orthodoxer Kalender \nAuswahl: "))

if o<1 or o>3:
    print("Keine Option wurde ausgewählt.")

## Aufgabe 1.2 ##
if o==1:
    j=int(input("Geben Sie ein Jahr ein: "))
    if (j%4)==0:
        print("Schaltjahr nach dem julianischen Kalender:", True)
    else:
        print("Schaltjahr nach dem julianischen Kalender:", False)


## Aufgabe 1.3 ##
if o==2:
    j=int(input("Geben Sie ein Jahr ein: "))
    if (j%4)==0:
        if (j%100)==0 and not (j%400)==0: 
            print("Schaltjahr nach dem gregorianischen Kalender:", False)
        else:    
            print("Schaltjahr nach dem gregorianischen Kalender:", True) 
    else:
        print("Schaltjahr nach dem gregorianischen Kalender:", False)



## Aufgabe 1.4 ##
if o==3:
    j=int(input("Geben Sie ein Jahr ein: "))
    if (j%4)==0:
        if (j%100)==0 and not ((j%900)==200 or (j%900)==600):
            print("Schaltjahr nach dem orthodoxen Kalender:", False)
        else:
            print("Schaltjahr nach dem orthodoxen Kalender:", True)
    else:
        print("Schaltjahr nach dem orthodoxen Kalender:", False)








