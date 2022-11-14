#큐 예제
from collections import deque

queue=deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.append(2)
queue.append(1)

queue.popleft()
queue.popleft()
#먼저 들어온게 삭제됨

print(queue)
queue.reverse()
print(queue)


print(list(queue)) #내용물만 빼오고 싶음



