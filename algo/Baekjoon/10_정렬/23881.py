# n, k = map(int, input().split())
# N = list(input().split())
N = [3, 1, 2, 5, 4]
cnt = 0
for i in range(len(N)-1, -1, -1):
    max = i
    for j in range(i-1, -1, -1):  # (len(N)-1, i, -1)
        if N[max] < N[j]:
            # cnt += 1
            # if cnt == k:
            #     a, b = N[max], N[j]

            # if cnt == 4 and cnt > 4:
            #     print(f'{N[max]},{N[j]}')
            # elif cnt != 4 and cnt < 4:
            #     print(-1)
            max = j
    N[max], N[i] = N[i], N[max]  # i랑 바꿔야하는 이유는?
    # i(max)를 기준으로 j와 비교를 했고 그에 따라 J가 크다는 타당성이 생겼음 즉 max가 j가 되고 각 둘을 스위치 한다.
    # print(N)

# if cnt > k:
#     print(a, b)
# else:
#     print(-1)


print(N)
# print(f"{N}, => {cnt}")


# for i in range(len(N)):
#     min = i
#     print(N)
#     for j in range(i+1, len(N)):
#         if N[min] > N[j]:
#             print(f'{N[i]}')
#             min = j
#             cnt += 1
#             # print(N[j])
#     N[min], N[i] = N[i], N[min]
