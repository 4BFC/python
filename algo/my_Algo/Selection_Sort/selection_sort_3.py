arr = [7, 5, 9, 0, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    min = i  # index를 기준으로 값을 비교한다.
    for ii in range(i+1, len(arr)):
        if arr[min] > arr[ii]:
            min = ii  # 5
        print(ii, arr)
    arr[min], arr[i] = arr[i], arr[min]  # 5, 7
print(arr)
