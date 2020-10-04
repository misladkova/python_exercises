n = int(input())
cisla = []
x = input()
x2 = x.split()
#print('hjfhj', x2)
for i in x2:
    #print('gf', i)
    j = int(i)
    cisla.append(j)
x = int(input())    
for i in range(n):
    if i<(n-1):
        print(cisla[i]+x, end = ' ')
    else:
        print(cisla[i]+x, end = '')
print()
