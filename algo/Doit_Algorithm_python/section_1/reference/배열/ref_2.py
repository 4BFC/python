array = [1, 8, 7, 4, 3, 5, 6]
# n = len(array)
prefix_sum = [0] * (len(array) + 1)
print(f'{prefix_sum}')
for i in range(len(array)):
    print(f'{i}',end=' ')
    prefix_sum[i + 1] = prefix_sum[i] + array[i]
    print(prefix_sum)
print()
print(prefix_sum)