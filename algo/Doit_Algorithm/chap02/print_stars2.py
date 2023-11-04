# *를 n개 출력하되 w개마다 줄바꿈하기 2

print('*를 출력합니다.')
n = int(input('몇 개를 출력할까요?: '))  # 9
w = int(input('몇 개마다 줄바꿈할까요?: '))  # 3

for _ in range(n//w):  # 3
    print('*' * w)  # 3개씩
# 여기서 이전 방법과는 달리 print()를 기입하지 않아도 된다.
rest = n % w  # 나머지 0 0은 FALSE, 즉, 출력후 나머지 출력하기.
if rest:
    print('*' * rest)
