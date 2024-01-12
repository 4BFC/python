N = [3, 1, 2, 5, 4]
cnt = 0
k = 2
for last in range(len(N)-1, -1, -1):
    max = last
    for j in range(last, -1, -1):  # 가장 큰 수를 찾는 loop
        if N[max] < N[j]:  # 가장 큰 수 판별
            # switch
            N[max], N[j] = N[j], N[max]  # 방법 1

print(N)
