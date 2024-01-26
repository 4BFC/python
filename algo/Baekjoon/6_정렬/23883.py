# heap을 알아야함.
import sys
n, k = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
cnt = 0


def selection_sort(arr):
    global cnt
    for i in range(len(arr)):
        _max = arr.index(max(arr[:i+1]))
        if _max != i:
            cnt += 1
            arr[_max], arr[i] = arr[i], arr[_max]
            if cnt == k:
                print(arr[_max], arr[i])
    if cnt < k:
        print(-1)


selection_sort(N)
