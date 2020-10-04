n = int(input())
cisla = []
x = input()
y = x.split()
for i in y:
    j = int(i)
    cisla.append(j)
x = int(input())
mensie = []
for i in cisla:
    if i<x:
        j = int(i)
        mensie.append(int(j))
print(sum(mensie))
        

