t= int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    p = 1
    for j in range(n):
        if a[j]<=j+1:
            p=j+2
    print(p)
