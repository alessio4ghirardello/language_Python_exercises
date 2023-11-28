a= []
n = 0
while n < 5:
    a.append(input('Inserisci un numero: '))
    n = n+1

for i in a:
    if int(i) % 2 == 0:
        print(i)

for i in a:
    if int(i) % 2 != 0:
        print(i)