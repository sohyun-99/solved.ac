L,R=map(int,input().split())
Min=R
if L==R:
    count=0
    l=list(str(L))  
    for i in range(len(l)):
        if l[i]=="8":
            count+=1
else :
    for k in range(L,R):
        count=0
        l=list(str(k))
        for i in range(len(l)):
            if l[i]=="8":
                count+=1
        if count<Min:
            Min=count
        if count==0:
            break
print(Min)
