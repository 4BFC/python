import sys
input = sys.stdin.readline
n = int(input())


def POP(N):
    while '()' in N:
        N = N.replace('()', '')
    # print(N)
    # print(len(N))
    if len(N) != 0:
        print('NO')
    else:
        print('YES')


for _ in range(n):
    N = input().strip()
    POP(N)
