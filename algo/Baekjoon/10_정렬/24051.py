N = [4, 5, 1, 3, 2]
n = 5
k = 7
cnt = 0
# for i in range(1, len(N)):
#     for j in range(i, 0, -1):
#         # print(N[j])
#         if N[j] < N[j-1]:
#             cnt += 1
#             if cnt == 4 :
#                 print(N[j],N[j-1])
#             N[j],N[j-1] = N[j-1],N[j]
# print(cnt)
# print(N)

for i in range(1, len(N)):
    std = i
    for j in range(len(N)):
        if N[std] < N[j]:
            cnt += 1
            N[std],N[j] = N[j],N[std]
print(cnt)
print(N)