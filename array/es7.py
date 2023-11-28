ar = []

while True:
    numero = int(input("Inserisci un numero:"))
    
    if(numero == 0):
        if(len(ar) % 2 == 0):
            print("la somma è pari")
        else:
            print("la somma è dispari")
        break

    if(numero > 0):
        ar.append(numero)
   