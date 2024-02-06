import sys 
input = sys.stdin.readline

n = int(input())
N = [0] * (10000+1)

for _ in range(n):
    N[int(input())] += 1

# 특정 값의 빈도 확인
# x = int(input())
# print(N.index(2))
for i in range(len(N)):
    if N[i] != 0 :
        for _ in range(N[i]): #? 여기가 왜 => 몇번 등장했는지 확인하는 코드이다.
            print(i)
