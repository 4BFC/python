#지나치게 많은 sum 때문에 그렇다 그러니 sum을 최소화 하는 방법을 생각해 보자.
#https://531522szerodesire.tistory.com/87
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
array = list(map(int,input().split()))

# pre_array = [0] * N
pre_array = []
for i in range(N): #start,end,step
    print(array[i:K+i])
    # pre_array[i] = sum(array[i:K+i])
    pre_array.append(sum(array[i:K+i]))
    print(pre_array)
print(max(pre_array))
# print(max(SUM))
#     pre_array[i+1] = pre_array[i] + array[i]
#     print(pre_array)
# print(pre_array)