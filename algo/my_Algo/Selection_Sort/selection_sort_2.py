arr = [7, 5, 9, 0, 1, 6, 2, 4, 8]
for i in arr:  # 비교값
    min = i
    for ii in arr:
        if min > ii:
            print(i)
            min = ii

    # switch를 하기 위해선 index를 이용해야한다
    # for ii in range(1,len(arr)):
        # if min < arr[ii] :
           # print(arr[ii])
           # min = arr[ii]
