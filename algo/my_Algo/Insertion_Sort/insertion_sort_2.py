array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i-1, 0, -1):  # 왜 역순인지 이해가 안감..
        print(j)
        print(f"{array[j]} < {array[j-1]}")
        if array[j] < array[j-1]:  # i번째랑 바꾸면 기준인 i의 값과 혼동이 된다.
            array[j-1], array[j] = array[j], array[j-1]
        else:
            break
    #     print(array)
    # print(f"{array[i]} < {array[i-1]}")

# print(array)
