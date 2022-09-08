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
_sum=0
A=0
rest=[]
_rest=0

# num<K 로 만들어야함
num=num//2
num_rest=num%2
#나머지가 있으면 num개 만큼의 같은 리터에대가 따로노는 애 1명

def countSum(num,A) :
    if num > 1:
        num=num//2
        if num%2==1:
            rest.append(2**A)
        _sum+=num+num%2   
        A+=1
    else:
        A+=2

countSum(num,A)
while _sum > K:
    countSum(num,A)
print(_sum)
print(rest)
print(A)
##while _sum > K:
##    for i in range(len(rest)):
##        if rest[i] != rest[i+1]:
##            rest+=rest[i+1]-rest[i]
##        else:
##            rest[i]=2*rest[i]
##            rest.pop(rest[i])
        

        

    
