N = [3, 1, 2, 5, 4]
cnt = 0
k = 2
print(len(N))
for last in range(len(N)-1, -1, -1):
    max = last
    for j in range(last, -1, -1):  # 가장 큰 수를 찾는 loop
        if N[max] < N[j]:  # 가장 큰 수 판별
            max = j  # ?
            # N[max], N[last] = N[last], N[max] #방법 1
            # switch
    # ? -> i(max)와 last가 같다는 것은 max값을 재설정(max = j)하지 않았다는 것이다. 즉, 그것을 판별 하기 위함이다.
    if last != max:
        N[max], N[last] = N[last], N[max]
        cnt += 1
        if cnt == k:
            print(N[max], N[last])
            exit()
print(-1)
# N[max], N[j] = N[j], N[max]  # switch 틀린 방법은 아니지만 직접적으로 최대값을 찾아서 교체하는 방법이 아니다.


print(N)
print(len(N))
print(cnt)
