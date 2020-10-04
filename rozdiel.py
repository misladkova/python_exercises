riadok1 = input()
riadok2 = input()
riadok1 = riadok1.split()
riadok2 = riadok2.split()
cisla = []
for i in riadok2:
    j = int(i)
    cisla.append(j)
n = int(riadok1[0])
x = int(riadok1[1])
nasiel = False
for i in range(n):
    for j in range(n):
        m = cisla[i]-cisla[j]
        if m == x:
           nasiel = True
if nasiel == True:
    print('Ano')
else:
    print('Nie')
