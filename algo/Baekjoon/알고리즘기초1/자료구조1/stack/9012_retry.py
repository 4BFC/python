# split을 다시 공부해보자.
import sys
N = int(sys.stdin.readline())
temp = []
for _ in range(N):
    # VPS = sys.stdin.readline().split()
    VPS = input().split()
    res = VPS
    test = "test"
    print(type(res))
    print(list(test))
    # temp.append(VPS)
print(temp)
