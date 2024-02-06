from collections import deque
# 현재는 enque인 정 방향으로만 존재하는 que이다. 
#이와 반대인 deque가 있는데 이는 따로 다시 실습할 것이다.
# 빈 deque 생성
my_deque = deque()

# 오른쪽에 원소 추가
my_deque.append(1)
my_deque.append(2)
my_deque.append(3)

# 왼쪽에서 원소 추가
my_deque.appendleft(0)

# 현재 deque 출력
print("현재 deque:", my_deque)

# 오른쪽에서 원소 제거
removed_element = my_deque.pop()

# 왼쪽에서 원소 제거
removed_left_element = my_deque.popleft()

# 제거 후 deque 출력
print("제거된 오른쪽 원소:", removed_element)
print("제거된 왼쪽 원소:", removed_left_element)
print("현재 deque:", my_deque)
