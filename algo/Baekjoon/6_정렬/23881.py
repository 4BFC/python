# n, k = map(int, input().split())
# N = list(input().split())
N = [3, 1, 2, 5, 4]
cnt = 0
for i in range(len(N)-1, -1, -1):
    max = i
    for ii in range(i-1, -1, -1):  # (len(N)-1, i, -1)
        if N[max] < N[ii]:
            # cnt += 1
            # if cnt == k:
            #     a, b = N[max], N[ii]

            # if cnt == 4 and cnt > 4:
            #     print(f'{N[max]},{N[ii]}')
            # elif cnt != 4 and cnt < 4:
            #     print(-1)
            max = ii
    N[max], N[i] = N[i], N[max]
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
#     for ii in range(i+1, len(N)):
#         if N[min] > N[ii]:
#             print(f'{N[i]}')
#             min = ii
#             cnt += 1
#             # print(N[ii])
#     N[min], N[i] = N[i], N[min]
