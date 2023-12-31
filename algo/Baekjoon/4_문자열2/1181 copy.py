N = ['but', 'i', 'wont', 'hesitate', 'no', 'more',
     'no', 'more', 'it', 'cannot', 'wait', 'im', 'yours']

# 선택 정렬 알고리즘 직접 구현
for i in range(len(N)):  # N의 배열 길이를 i로 반환
    min_index = i
    for j in range(i + 1, len(N)):  # 1에서부터 N의 배열 길이 만큼
        # 첫번째 for문이 i(min_index)일때 i를 기준으로 j로 반환된 전체 길이만큼 루프가 돈다.
        # print(j, end=' ')
        # min_index를 정하는 if문이다.
        # 1 과 0 index를 비교
        if len(N[j]) < len(N[min_index]) or (len(N[j]) == len(N[min_index]) and N[j] < N[min_index]):
            # N[j] < N[min_index] 알파벳의 순서크기 비교
            min_index = j

    N[i], N[min_index] = N[min_index], N[i]  # 서로 switch하는 구문
    print(N)
# 중복 제거
unique_N = []
for item in N:
    if item not in unique_N:  # unique_N list에 요소가 없을 때
        unique_N.append(item)

# 결과 출력
for item in unique_N:
    print(item)
