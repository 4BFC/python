N, M = map(int, input().split())  # 5(공의 위치),4(공을 바꿀 수 있는 횟수)
basket = []
# * (N+1)
for i in range(N):  # 1, N+1
    basket.append(i+1)
for _ in range(M):
    # swap
    i, j = map(int, input().split())  # i 바꾸고 싶은 공 위치 ,j 바꿀 공 위치
    temp = basket[i-1]
    basket[i-1] = basket[j-1]
    basket[j-1] = temp

for _ in range(len(basket)):
    print(basket[_], end=" ")
