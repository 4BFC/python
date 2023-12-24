N = []
for _ in range(ord('A'), (ord('Z')+1)):
    N.append(chr(_))
# for _ in range(len(N)):
#     print(f"{_}:{N[_]}", end=" ")
# print()
# for문으로 알파벳 찾기
# for _ in N:
#     print(_, end=" ")
# print()
input = input()
cnt = 2
for _ in input:
    # print(N.index(_), end=" ")

    if N.index(_) < 3:
        cnt += 2
    elif N.index(_) < 6:
        cnt += 3
    elif N.index(_) < 9:
        cnt += 4
    elif N.index(_) < 12:
        cnt += 5
    elif N.index(_) < 15:
        cnt += 6
    elif N.index(_) < 19:
        cnt += 7
    elif N.index(_) < 22:
        cnt += 8
    elif N.index(_) < 26:
        cnt += 9
print(cnt)
# U(8)N(6)U(8)C(2)I(4)C(2)
# 24
# print(N[0:3]) #특정 범위 지정으로 해당 값들의 증가 단위 설정
# if N[]

# for i in range(len(N)):
#     print(N[i])
