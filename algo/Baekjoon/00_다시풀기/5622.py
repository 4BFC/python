N = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
n = 'WA'

# 오로지 문자열로만 for문을 나열 했다.

for i in n:  # n 문자열 i로 해체
    # print(i)
    for ii in N:  # N 문자열 ii로 해체
        # print(ii)
        if i in ii:  # n in N
            print(f"{i} / {i in ii}")  # 읽는 방향 ->
            print(n.index('A'))
        # print(f"{N.index(ii)} / {i} in {ii}")
