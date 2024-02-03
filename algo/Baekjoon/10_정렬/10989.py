import sys
input = sys.stdin.readline
n = int(input())
N = []
for _ in range(n):
    N.append(int(input()))
N.sort()
# print(*N)
for i in range(len(N)):
    print(N[i])
