from collections import deque

queue = deque()

queue.append(1)
queue.append(2)
queue.append(3)

first_item = queue.pop()
second_item = queue.pop()

print(first_item)
print(second_item)
print(queue)
