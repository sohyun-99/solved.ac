L,R=map(int,input().split())
Min=0
l=str(L)
r=str(R)

if len(str(L))!=len(str(R)):
    Min=0
else :
    for i in range(len(str(R))):
        if l[i]==r[i]:
            if l[i]=='8':
                Min+=1
        else:
            break
print(Min)
