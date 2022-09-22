N=int(input())
TS=[list(map(int,input().split())) for _ in range(N)]
TS.sort(key=lambda x:(x[1],x[0]), reverse=True)

first=TS[0][1]-TS[0][0]
blank=0

print(TS)
for i in range(1,N):
    if TS[i][1]>=first:
        first-=TS[i][0]
    else:
        first=TS[i][1]-TS[i][0]

    if first<0:
        first=-1
        break
                     
print(first)
##blank처리를 잘 해주지 못해 올바른 답 도출 실패
