n = int(input())
cisla = []
for i in range(n):
    riadok = list(map(int, input().split()))
    cisla.append(riadok)
for x in range(n):
    for y in range(n):
        a = y
        b = n-1-x
        k = cisla[a][b]
        if y != n-1:
            print(k, end = ' ')
        else:
           print(k, end = '')
    print()