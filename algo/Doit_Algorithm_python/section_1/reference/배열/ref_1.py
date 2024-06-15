array = [1, 8, 7, 4, 3, 5, 6]
# n = len(array)
prefix_sum = [0] * len(array)

for i in range(len(array)):
    print()
    for j in range(i+1):
        print(f'{j}',end=' ')
        prefix_sum[i] += array[j]
print()
print(prefix_sum)