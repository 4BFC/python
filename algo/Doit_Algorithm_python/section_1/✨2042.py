N,M,K = 5, 2, 2
array = [1,2,3,4,5]
pre_array = [0] * (len(array)+1 )
print(pre_array)
# for i in N :
#     input()
for i in range(len(array)):
    pre_array[i+1] = pre_array[i] + array[i]
    print(pre_array)
print(pre_array)