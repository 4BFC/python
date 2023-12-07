# dequeue
from collections import deque
print("dequeue")
queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

first_item = queue.popleft()
second_item = queue.popleft()

print(first_item)
print(second_item)
print(queue)
