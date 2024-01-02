N = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = input()

# 문자열과 int로 for을 돌렸다.
result = []
for i in n:  # n 문자열 i로 해체
    # print(i)
    for ii in range(len(N)):  # N 문자열 ii로 해체
        # print(N[ii])
        if i in N[ii]:  # n in N
            print(f"{i} / {i in N[ii]}")  # 읽는 방향 ->
            print(ii + 2)
            result.append(ii+2)
            # -> ii를 통해서 해당 위치의 인덱스 값을 알 수 있다.
            # 이를 gpt를 통해 알게 되었다만 더 고민하고 코드에 필요한 사고를 기를 수 있으면 좋겠다.
            # print(N[ii])
        # print(f"{N.index(ii)} / {i} in {ii}")

print(sum(result)+len(result))
