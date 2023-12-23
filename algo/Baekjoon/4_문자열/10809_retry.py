N = list(str(input()))
c = ""
for _ in range(97, 122+1):
    c += chr(_)

for i in c:  # c가 i로 알파벳을 반환한다.
    if i in N:  # 만약 N의 값이 i에 있다면 True
        print(N.index(i), end=' ')  # N을 기준으로 i의 값의 index값을 반환한다.
    else:
        print(-1, end=' ')
