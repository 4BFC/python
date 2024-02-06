#FIFO 이기때문에 먼저 들어간 인자가 먼저 나온다. stack과 반대이다.
from collections import deque

queue = deque([1,2,3])
queue.append(4)
print(queue)
print(queue.popleft())
print(queue)

queue.append(5)
print(queue)
print(queue.pop())
print(queue)
