#미로 탈출

from collections import deque

n,m=map(int,input().split())
list=[list(map(int,input().strip())) for _ in range(n)]


dx=[-1,+1,0,0]
dy=[0,0,-1,+1]

#def bfs(n,m,list):
queue=deque()
queue.append((0,0))

while queue:
    i,j=queue.popleft()
    print(i,j)
    for a in range(4):
        x=i+dx[a]
        y=j+dy[a]
        if x<0 or y<0 or x>=n or y>=m :
            continue
        if list[x][y]==1:
            queue.append((x,y))
            list[x][y]=list[i][j]+1 #전 위치 기준으로 +1 해주면서 처음부터 이곳까지를 보는겨
            
            
print(list[n-1][m-1])
