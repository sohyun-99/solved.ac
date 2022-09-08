N=input("")
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort() # A값을 오름차순으로 정렬

Max_index=0
result=0
for i in range(int(N)):
    Max=0
    for n in range(len(B)):
        if B[n-1]>=Max:
            Max=B[n-1]
            Max_index=n-1
    B.pop(Max_index)
    result+=Max*A[i]
print(result)
