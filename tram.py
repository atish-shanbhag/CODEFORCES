c=m=0
for i in range(int(input())):
    a,b=map(int,input().split())
    c=c+b-a
    m=max(m,c)
print(m)