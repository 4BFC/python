N = [3, 1, 2, 5, 4]
cnt = 0
K = 2
for last in range(len(N)-1, -1, -1):
    max = last
    for j in range(last, -1, -1):
        if N[max] < N[j]:
            max = j
    if last != max:  # 여기를 틀림.. 이건 문제를 잘 보지 못한 것임..
        N[max], N[last] = N[last], N[max]
        cnt += 1
        if cnt == K:
            print(N[max], N[last])
            exit()

print(-1)
print(N)
