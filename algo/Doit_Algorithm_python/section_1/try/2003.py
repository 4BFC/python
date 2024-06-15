# N,M = 4,2
# N = [1,1,1,1]

import sys
input = sys.stdin.readline

N,M = map(int, input().split())
N = list(map(int, input().split()))

prefix_sum = [0] * (len(N)+1)

for i in range(len(N)):
    prefix_sum[i+1] = prefix_sum[i] + N[i]
    if i == M : 
        print(prefix_sum[i+1])
print(prefix_sum)