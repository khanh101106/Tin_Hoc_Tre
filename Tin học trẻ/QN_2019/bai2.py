a=input();print(len(set(a)))
print(len(a))
b=[]
for i in range(len(a)-1):
    for j in range(i+1,len(a)):
        b.append(len(set(a[i:j+1])))
for i in range(2,max(b)+1):
    print(b.count(i))