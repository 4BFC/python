N, M = map(int, input().split())  # 5 4
basket = [0] * (N+1)  # 6까지
print(basket)
for _ in range(M):  # 4
    i, j, k = map(int, input().split())  # 1 2 3
    print(_)
    for n in range(i, j+1):  # [0,1,2,3,4] 5 0,1,2,3/4 index
        basket[n] = k
        print(basket)

for _ in range(1, N+1):  # start, end, step
    print(basket[_], end=" ")
