array = [1, 8, 7, 4, 3, 5, 6]
n = len(array)
prefix_sum = [0] * (n + 1)
x, y = 1, 5

for i in range(n):
    print(f'{prefix_sum[i + 1]} = {prefix_sum[i]} + {array[i]}')
    prefix_sum[i + 1] = prefix_sum[i] + array[i]
    print(prefix_sum)
        
part_sum = prefix_sum[y] - prefix_sum[x - 1]
print(part_sum)