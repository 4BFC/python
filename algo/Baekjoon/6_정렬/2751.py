import sys
n = sys.stdin.readline()
N = []
for i in range(int(n)):
    N.append(int(sys.stdin.readline()))
N.sort()
# N.reverse()
for i in range(len(N)):
    print(N[i])
