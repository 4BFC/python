#지나치게 많은 sum 때문에 그렇다 그러니 sum을 최소화 하는 방법을 생각해 보자.
#https://531522szerodesire.tistory.com/87
import sys
input = sys.stdin.readline

N,K = map(int,input().split())
array = list(map(int,input().split()))

pre_array = []
print(array[:K])
print(array)
pre_array.append(sum(array[:K]))
print(pre_array)
# pre_array = [0] * N #-> 더 적극적으로 활용해 볼 것
for i in range(N-K): 
    #sum(array[i:K+i])
    # print(f'{array[i]} + {array[i+K]} = {array[i] + array[i+K]}')
    # pre_array.append(array[i] + array[i+K])
    print(f'{pre_array[i]} - {array[i]} + {array[i+K]}')
    print(pre_array)
    pre_array.append(pre_array[i] - array[i] + array[i+K])

print(pre_array)
# print(max(pre_array))