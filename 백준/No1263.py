N=int(input())
TS=[list(map(int,input().split())) for _ in range(N)]
TS.sort(key=lambda x:(x[1],x[0]))

first=TS[0][1]-TS[0][0]
blank=0


for i in range(N-1):
    Trest=TS[i+1][1]-TS[i+1][0]
    if TS[i][1]>Trest:
        if blank-(TS[i][1]-(Trest))<0:
            first+=blank-(TS[i][1]-(Trest))
            blank=0
        else:
            blank=blank-(TS[i][1]-(Trest))
    elif TS[i][1]<Trest:
        blank+=Trest-TS[i][1]
                     

summ=0
for i in range(N):
    summ+=TS[i][0]
    if(summ>24):
        first=-1

print(first)
##blank처리를 잘 해주지 못해 올바른 답 도출 실패
