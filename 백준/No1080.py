N,M = map(int,input().split())
list_a=[list(map(int,input().rstrip())) for _ in range(N)] #2차원 배열 선언
list_b=[list(map(int,input().rstrip())) for _ in range(N)] #2차원 배열 선언

def makeit(i,j): #변환해주는 함수 
    for k in range(i,i+3):
        for m in range(j,j+3):
            if list_a[k][m]==0:
               list_a[k][m]=1 
            else :
               list_a[k][m]=0
    return list_a

def checkit():
    if list_a==list_b:
        return True
    return False
n=0
breaker=False
for i in range(N-2):
    for j in range(M-2):
        if list_a[i][j] != list_b[i][j]:
            makeit(i,j)
            n+=1
            if checkit()==True:
                breaker=True
                break
    if breaker==True  :
        break
if checkit()==False:
    n=-1
print(n)
