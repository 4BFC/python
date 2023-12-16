import math
T = input()

for i in range(int(T)):
    A, B = map(int, input().split())
    print(math.lcm(A, B))
