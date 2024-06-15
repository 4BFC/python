N, M = 4, 2
array = [1, 1, 1, 1]
pre_array = [0] * (len(array)+1)
print(pre_array)
for i in range(len(array)):
    pre_array[i+1] = pre_array[i] + array[i]
    # pre_array[i+1]를 더해야 하는 이유는?
print(pre_array)
