#n개의 물병
#물병에는물이 1리터씩
#K개를 한번에 옮길예정
#총 n리터인데 이 물들을 재분배
#같은양의 물 2개를 골라 -> 한쪽으로 몰아 -> 반복
#k개를 넘지 않는 비어있지않은 물병만들기
#만약에 불가능할 경우 1l를 어있는 물병 사면됨


N,K=map(int,input().split()) #총 n개의 물병을 한번에 K개 옮길 수 있음


#비어있지 않은 총 물병의갯수
num=N
A=0
rest=[]
#_rest=0
answer=0
i=0

 #현재 담겨있는 물병의 갯수
_sum=N

#그 갯수가 K보다 같거나 작아질때까지 while문 돌림
while _sum > K: 
    if num>1 :
        if num%2==1:#남는 물병이 존재한다는 뜻
            rest.append(2**A)
        num=num//2
        _sum=num+len(rest)
        A+=1
    else:
        if(i<len(rest)-1):
            answer+=rest[i+1]-rest[i]
            rest[i+1]*=2
            _sum-=1
            i+=1
        else:
            if len(rest)==1:
                answer=2**A-rest[0]
                _sum-=1
            else:
                if _sum==2:
                    answer+=2**A-rest.pop()
                break

print(answer) #구매해야하는 물병의 수

        

        

    
