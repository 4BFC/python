N = int(input())
N_list = list(map(int, input().split()))
min = N_list[0]
max = N_list[0]
for _ in range(N):
    if max < N_list[_]:
        max = N_list[_]
        # print(N_list[_])

    elif min > N_list[_]:
        min = N_list[_]
        # print(N_list[_])
print(f"{min} {max}")
