import sys
input = sys.stdin.readline
N = []
for _ in range(5):
    N.append(int(input()))
#split을 사용하면 list이다.
for i in range(1,len(N)):
    std = i
    for j in range(len(N)):
        if N[std] < N[j]:
            N[std],N[j] = N[j],N[std]
# print(N)
print(round(sum(N)/len(N)))
print(N[2])
#1 2 3 4 5 6 7 8 9
# 10
# 40
# 30
# 60
# 30