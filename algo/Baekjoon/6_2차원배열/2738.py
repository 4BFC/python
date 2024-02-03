#https://develop247.tistory.com/93
import sys
input = sys.stdin.readline
# N,M = map(int,input().split())
# print("test")
n = input().split()

# print(n)
# print(len(n))
N = []

for i in range(len(n)):
    for ii in range(int(n[0])) :
        row = list(map(int,input().split()))
        N.append(row)
# print(N[0] + N[1])
for i in range(int(n[0])):
    result = [a + b for a, b in zip(N[i], N[i+3])]
    print(*result)
# `print(N[2])
# print(N[3])`

# N = [input().split() for _ in range(len(n)) for _ in range(int(n[0]))]

print(N)

# 1 1 1
# 2 2 2
# 0 1 0
# 3 3 3
# 4 4 4
# 5 5 100