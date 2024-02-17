import sys 
input = sys.stdin.readline

N,K = map(int,input().split())

array = list(map(int,input().split()))
pre_array = [sum(array[:K])]
# print(pre_array)

for i in range(N-K) : 
    pre_array.append(pre_array[i] - array[i] + array[i+K])
print(max(pre_array))