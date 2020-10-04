n = int(input())
k = (2*n//2)-1
m = 1
j = (2*n//2)-1
for r in range(0, n):
    for c in range(0, k):
        print('.', end = '')
    k = k-1
    for c in range(0, m):
        print('*', end = '')
    m = m+2
    for c in range(0, j):
        print('.', end = '')
    j = j-1  
    print()
    
