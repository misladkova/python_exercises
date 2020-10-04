n = int(input())
a = 0
b = 1
if n<= 0:
    print(n)
else:
    print(a, b, end = ' ')
    for i in range(2,n):
        c = a + b
        if i<n-1:
            print(c, end = ' ')
        else:
            print(c, end='')
        a = b
        b = c
print()







        
    
        
