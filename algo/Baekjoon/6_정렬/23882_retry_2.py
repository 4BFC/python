import sys
n, k = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
cnt = 0


def selection_sort(arr):
    global cnt
    for last in range(len(arr)-1, -1, -1):
        max = last
        for j in range(last, -1, -1):
            if arr[max] < arr[j]:
                max = j
        if last != max:
            arr[max], arr[last] = arr[last], arr[max]  # 왜 max와 last 를 바꾸는가
            cnt += 1
        if cnt == k:
            print(*arr)
            exit()
    print(-1)


selection_sort(N)
