N = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for std in range(1, len(N)):  # 5(2)
    for j in range(std, 0, -1):  # 역순으로 감소(차감)하면서
        print(j, end=" ")
        if N[j] < N[j-1]:  # 앞과 뒤를 살피면서 왼쪽으로 당겨야한다.
            N[j], N[j-1] = N[j-1], N[j]
    print(N)
# array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# for std in range(1, len(array)):
#     print(f"[{std}]")
#     for j in range(std, 0, -1):  # 왜 역순인지 이해가 안감..
#         # print(j)
#         print(f"{array[j]} < {array[j-1]}")
#         if array[j] < array[j-1]:  # i번째랑 바꾸면 기준인 i의 값과 혼동이 된다.
#             array[j-1], array[j] = array[j], array[j-1]
#         else:
#             break
#         print(array)