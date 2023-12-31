# input이 아닌 sys로 문제 다시 풀어볼 것.
# import sys
N = []
# l = sys.stdin.readlines()
l = input()

for i in range(int(l)):
    n = input()

    if len(n) > 2:
        N.append(n[2])

    if n == '2':
        if len(N) != 0:
            print(N.pop())
        elif len(N) == 0:
            print(-1)
    if n == '3':
        print(len(N))
    if n == '4':
        if len(N) == 0:
            print(1)
        else:
            print(0)
    if n == '5':
        if len(N) != 0:
            print(N[-1])
        else:
            print(-1)
