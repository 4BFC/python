# 이것도 삽입정렬 알고리즘의 일부이다.
# GPT에서 어떤 정렬 알고리즘인지 물어보자.
N = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
for i in range(1, len(N)):
    std = i  # 5
    for j in range(len(N)):
        if N[std] < N[j]:
            N[std], N[j] = N[j], N[std]
    print(N)
