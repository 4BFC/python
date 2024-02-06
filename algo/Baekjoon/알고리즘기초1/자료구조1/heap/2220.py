import sys
import heapq
input = sys.stdin.readline
# N = [1,2,3,4,5,6]
n = int(input())
N = []
for i in range(n) :
   N.append(i+1)

h = []
result = []
for i in range(len(N)):
    heapq.heappush(h,-N[i])
    print(h)
for j in range(len(h)):
    result.append(-heapq.heappop(h))
print(*result)