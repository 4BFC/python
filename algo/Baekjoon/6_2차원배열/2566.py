import sys
input = sys.stdin.readline

N = []

for _ in range(9):
    row = list(map(int,input().split()))
    N.append(row)
max = N[0][0]
for i in range(9) :
    for j in range(9) :
        # print(N[i][j])
        if max < N[i][j]:
            max = N[i][j]

for i in range(len(N)):
    if max in N[i]:
        pos_X = i+1
        pos_Y = (N[i].index(max))+1
        break
print(max)
print(pos_X,pos_Y)
