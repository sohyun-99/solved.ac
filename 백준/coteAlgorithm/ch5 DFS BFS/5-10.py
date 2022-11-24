#음료수 얼려먹기

N,M=map(int,input().split())
list=[list(map(int,input().strip())) for _ in range(N)]

def dfs(x,y):
    
    #애초에 범위를 벗어나면 함수 작동이 안되게 함
    if x<0 or x>=N or y<0 or y>=M:
        return False

    #아직 방문하지 않은 곳에 대해 입장
    if list[x][y]==0:
        #방문했다고 체크
        list[x][y]=1

        #상하좌우에 대해 재귀 호출
        dfs(x+1,y)
        dfs(x-1,y)
        dfs(x,y+1)
        dfs(x,y-1)
        return True
    return False

result=0
for i in range(N):
    for j in range(M):
        if dfs(i,j)==True:
            result+=1

print(result)
