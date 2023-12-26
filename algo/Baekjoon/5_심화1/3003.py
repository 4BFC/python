chess = [1, 1, 2, 2, 2, 8]
N = input().split()
for _ in range(len(chess)):
    N[_] = chess[_] - int(N[_])

for _ in range(len(chess)):
    print(N[_], end=" ")
