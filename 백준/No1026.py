N=int(input()) ##애초에 int로 입력값 받기
A=list(map(int,input().split()))
B=list(map(int,input().split()))
A.sort() # A값을 오름차순으로 정렬

result=0
for i in range(N):
    result+=A[i]*max(B)
    B.pop(B.index(max(B)))
print(result)    

##초기 알고리즘 .. 바보처럼 max, min 함수 안씀...수동으로 찾아줌
##Max_index=0
##result=0
##for i in range(N):
##    Max=0
##    for n in range(len(B)):
##        if B[n-1]>=Max:
##            Max=B[n-1]
##            Max_index=n-1
##    B.pop(Max_index)
##    result+=Max*A[i]
##print(result)

#얻은점
#입력 받을때 자료형대로 입력받기
#max,min,index 함수 사용법
