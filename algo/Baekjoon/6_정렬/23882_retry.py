import sys
# N = [3, 1, 2, 5, 4]
# n, k = 5, 2
# n, k = map(int, input().split())
# N = input().split()

n, k = map(int, sys.stdin.readline().split())
N = list(sys.stdin.readline().split())
cnt = 0


# def _print(N):
#     for i in range(len(N)):
#         print(int(N[i]), end=' ')


# def selection_sort(N):
# global cnt
for last in range(len(N)-1, -1, -1):
    max = last
    for j in range(last, -1, -1):
        if N[max] < N[j]:
            max = j
    if last != max:
        N[max], N[last] = N[last], N[max]  # 왜 max와 last 를 바꾸는가
        cnt += 1
    if cnt == k:
        for i in range(len(N)):
            print(int(N[i]), end=' ')
        exit()
print(-1)


# selection_sort(N)
