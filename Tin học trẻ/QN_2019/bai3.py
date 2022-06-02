a=int(input())
b=[int(x) for x in input().split()]
m=n=0;h=1
for i in range(len(b)-1):
    for j in range(i+1,len(b))[::-1]:
        for k in range(i,j+1):
            n+=h*b[k]
            h+=1
        m=max(m,n);n=0;h=1
print(m)