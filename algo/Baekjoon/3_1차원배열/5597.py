N_list = []
# T_list = []
for _ in range(28):
    N_list.append(_)

for _ in range(28):
    N = int(input())
    if N_list.index(N):
        continue
    else:
        print(int(N_list[_]))

    # # N_list[_].append(N)와 같이 특정 영역에 append를 사용할때는에러를 낸다.
