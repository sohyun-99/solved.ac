#크기가 N인 배열 A
#배열의 모든 수는 서로 다르다
#이 배열을 소트할때 연속된 두개의 원소만 교환가능
#교환 최대횟수는 S번
#소트한 결과= 사전순으로 가장 뒷서는 것을 출력
#최댓값을 앞으로 당겨오는게 가장 우선시 되는 알고리즘을 짜야한다

N=int(input())
A=list(map(int, input().split()))
S=int(input())


for i in range(N):
    idx=A.index(max(A[i: min(N, i + S + 1)]))
    for j in range(idx,i,-1):
        A[j],A[j-1]=A[j-1],A[j] #교환하는 부분
    S -= (idx - i)
    if S <= 0: break
    
print(*A)        

        
    
