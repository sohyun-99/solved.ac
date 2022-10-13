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
#맨뒤부터 채우기로 알고리즘 구현 성
