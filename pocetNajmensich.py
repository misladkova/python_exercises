n = int(input())
cisla = []
x = input()
y = x.split()
for i in y:
    j = int(i)
    cisla.append(j)
najmensie = []
z = min(cisla)
for i in cisla:
    if i == z:
        j = int(i)
        najmensie.append(j)
print(len(najmensie))
        
        

    
