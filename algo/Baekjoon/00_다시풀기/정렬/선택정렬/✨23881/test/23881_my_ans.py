import sys
n, k = map(int, sys.stdin.readline().split())
N = list(map(int, sys.stdin.readline().split()))
cnt = 0


def selection(N):
    global cnt

    for last in range(len(N)-1, -1, -1):
        max = last
        for j in range(last, -1, -1):
            if N[max] < N[j]:
                max = j

        if last != max:
            cnt += 1
            N[max], N[last] = N[last], N[max]
            if cnt == k:
                print(N[max], N[last])
                exit()
    print(-1)


selection(N)
