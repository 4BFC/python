N, M = map(int, input().split())
# basket = []

# 순서생성
# for _ in range(N):
#     basket.append(_+1)

basket = [_ for _ in range(1, N+1)]

# i부터 j까지의 순서
for _ in range(M):
    i, j = map(int, input().split())
    temp = basket[i-1:j]
    temp.reverse()
    basket[i-1:j] = temp
# 출력
for _ in range(N):
    print(basket[_], end=" ")
