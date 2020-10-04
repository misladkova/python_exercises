n = int(input())
cisla = []
x = input()
y = x.split()
for i in y:
    j = int(i)
    cisla.append(j)
#print(y)
for r in range(n - 1):
    kolkokrat=n-r-1
    cisla2 = []
    for p in range(kolkokrat):
        cislo = cisla[p]+cisla[p+1]
        if p == kolkokrat-1:
            print(cislo, end = '')
        else:
            print(cislo, end = ' ')
        cisla[p] = cislo
    print()

