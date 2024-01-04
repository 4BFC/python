n, exchange = map(int, input().split())
arr = list(map(int, input().split()))
index = 0
swap = 0

for i in range(n-1, 0, -1):
    index = i

    for j in range(1, i+1):
        if arr[j] > arr[i]:
            index = j

    if i != index:
        arr[i], arr[index] = arr[index], arr[i]
        swap += 1  # cnt
        if swap == exchange:
            print(arr[index], arr[i])
            exit()
        else:
            print(-1)

# print(-1)
