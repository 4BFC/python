n, k = map(int, input().split())
N = input().split()
cnt = 0

for last in range(len(N)-1, -1, -1):
    max = last
    for j in range(last, -1, -1):
        if N[max] < N[j]:
            max = j
    if last != max:
        cnt += 1
        N[max], N[last] = N[last], N[max]
        if cnt == k:
            print(N[max], N[last])
            exit()
print(-1)
# print(cnt)
# print(N)
