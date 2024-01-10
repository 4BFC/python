# x, y = 5, 2
N = [3, 1, 2, 5, 4]

for i in range(len(N)-1, 0, -1):
    max = i
    # print(N[i])
    for j in range(i, -1, -1):
        # print(f"{N[i]} {N[j]}")
        if N[max] < N[j]:
            max = j
            print(N[max])
            # 큰수부터 먼저 바꾼다..
            N[max], N[i] = N[i], N[max]

print(N)
