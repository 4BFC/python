N = [3, 1, 2, 5, 4]
k = 2
cnt = 0
for last in range(len(N)-1, -1, -1):
    _max = N.index(max(N[:last+1]))
    if _max != last:
        cnt += 1
        N[_max], N[last] = N[last], N[_max]
    if cnt == k:
        for i in range(len(N)):
            print(N[i], end=' ')
if k > cnt:
    print(-1)
