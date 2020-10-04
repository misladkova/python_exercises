riadok1 = input().split()
m = int(riadok1[0])
n = int(riadok1[1])
cisla = []
for i in range(m):
    riadok = list(map(int, input().split()))
    cisla.append(riadok)
for i in range(n):
    for j in range(m):
        k = cisla[j]
        k2 = k[i]
        if j == m-1:
            print(k2, end = '\n')
        else:
            print(k2, end = ' ')

