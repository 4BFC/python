N = [3, 1, 2, 5, 4]
cnt = 0
k = 2
for last in range(len(N)-1, -1, -1):
    max = last
    for j in range(last, -1, -1):  # 가장 큰 수를 찾는 loop
        if N[max] < N[j]:  # 가장 큰 수 판별
            max = j  # last(max)와 j를 바꾸는 것
            N[max], N[last] = N[last], N[max]  # 방법 1
            # switch
print(N)
