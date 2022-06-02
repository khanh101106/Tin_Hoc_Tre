a=int(input())
if a<6:print("NO")
else:
    def check(a):
        b="".join(set(str(a)))
        if b=="86" or b=="68" or b=="6" or b=="8":return True
    if check(a):print("YES")
    else:
        for i in range(6,a):
            if a%i==0:
                if check(i):print("YES");break
        else:print("NO")