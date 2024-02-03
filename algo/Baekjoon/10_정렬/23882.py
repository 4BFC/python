y, x = map(int, input().split())  # 2
N = list(input().split())  # ['3', '1', '2', '5', '4']
cnt = 0
n = ''

for i in range(len(N)-1, -1, -1):
    max = i
    # print(f"i : {N[i]}")
    for ii in range(i - 1, -1, -1):
        if N[max] < N[ii]:
            if cnt == x and len(N) > x:
                n = N.copy()
            else:
                # print(cnt)
                n = -1
            cnt += 1
            max = ii

        # print(f"ii : {N[ii]}")
    N[max], N[i] = N[i], N[max]
    # print(f"{N[ii]}")

print(n)
# print(cnt)
# print(N)
