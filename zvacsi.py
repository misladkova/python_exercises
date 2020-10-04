n = int(input())
x = int(input())
for i in range(n):
    y = int(input())
    z = y+x
    if i < (n-1):
        print(z, end = ' ')
    else:
        print(z, end = '')
print()
