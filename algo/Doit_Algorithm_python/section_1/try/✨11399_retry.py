import sys
input = sys.stdin.readline


n = int(input())
N = list(map(int,input().split()))
N.sort()
array = [0] * (len(N)+1)

for i in range(n) :
    array[i+1] = array[i] + N[i]
    
print(sum(array))