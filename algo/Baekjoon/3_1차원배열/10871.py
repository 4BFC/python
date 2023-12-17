N, X = map(int, input().split())
x_list = list(map(int, input().split()))
for i in range(N):
    if x_list[i] < X:
        print(x_list[i], end=" ")
