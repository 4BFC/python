N = [3, 1, 2, 5, 4]
cnt = 0
for i in range(len(N)):
    _max = N.index(max(N[:i+1]))
    if i != _max:
        N[i], N[_max] = N[_max], N[i]
        cnt += 1
        if cnt == 2:
            print(N[_max], N[i])
print(N)
